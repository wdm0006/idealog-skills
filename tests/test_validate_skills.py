#!/usr/bin/env python3
"""Fixture-driven tests for ``scripts/validate_skills.py`` (stdlib only).

Run with: ``python3 -m unittest discover -s tests``
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import validate_skills  # noqa: E402


def write_skill(repo_root, name):
    skill_dir = repo_root / "skills" / name
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Does {name} things.\n---\n\n# {name}\n",
        encoding="utf-8",
    )


def write_manifest(repo_root, plugins):
    manifest_dir = repo_root / ".claude-plugin"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    (manifest_dir / "marketplace.json").write_text(
        json.dumps({"name": "idealog-skills", "plugins": plugins}, indent=2),
        encoding="utf-8",
    )


def complete(skills):
    return {"name": "idealog-complete", "source": "./", "strict": False, "skills": skills}


class CompleteBundleCoverageTest(unittest.TestCase):
    """Every skill on disk must appear in ``idealog-complete`` exactly once."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        for name in ("alpha-skill", "beta-skill"):
            write_skill(self.root, name)

    def test_full_coverage_passes(self):
        write_manifest(self.root, [complete(["./skills/alpha-skill", "./skills/beta-skill"])])
        self.assertEqual(validate_skills.collect_errors(self.root), [])

    def test_missing_skill_fails(self):
        write_manifest(self.root, [complete(["./skills/alpha-skill"])])
        errors = validate_skills.collect_errors(self.root)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("idealog-complete", errors[0])
        self.assertIn("./skills/beta-skill", errors[0])

    def test_duplicate_skill_fails(self):
        write_manifest(
            self.root,
            [complete(["./skills/alpha-skill", "./skills/beta-skill", "./skills/alpha-skill"])],
        )
        errors = validate_skills.collect_errors(self.root)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("listed 2 times", errors[0])
        self.assertIn("./skills/alpha-skill", errors[0])

    def test_equivalent_path_spellings_count_as_duplicates(self):
        write_manifest(
            self.root,
            [complete(["./skills/alpha-skill", "skills/alpha-skill/", "./skills/beta-skill"])],
        )
        errors = validate_skills.collect_errors(self.root)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("listed 2 times", errors[0])

    def test_curated_subset_bundle_may_omit_skills(self):
        write_manifest(
            self.root,
            [
                complete(["./skills/alpha-skill", "./skills/beta-skill"]),
                {
                    "name": "idealog-essentials",
                    "source": "./",
                    "strict": False,
                    "skills": ["./skills/alpha-skill"],
                },
            ],
        )
        self.assertEqual(validate_skills.collect_errors(self.root), [])

    def test_absent_complete_bundle_fails(self):
        write_manifest(
            self.root,
            [
                {
                    "name": "idealog-essentials",
                    "source": "./",
                    "strict": False,
                    "skills": ["./skills/alpha-skill", "./skills/beta-skill"],
                }
            ],
        )
        errors = validate_skills.collect_errors(self.root)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("no plugin named 'idealog-complete'", errors[0])

    def test_directory_without_skill_md_is_not_required(self):
        (self.root / "skills" / "not-a-skill").mkdir()
        write_manifest(self.root, [complete(["./skills/alpha-skill", "./skills/beta-skill"])])
        self.assertEqual(validate_skills.collect_errors(self.root), [])


class ExistingChecksTest(unittest.TestCase):
    """The pre-existing manifest-path and frontmatter checks still fire."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_declared_path_must_exist(self):
        write_skill(self.root, "alpha-skill")
        write_manifest(self.root, [complete(["./skills/alpha-skill", "./skills/ghost-skill"])])
        errors = validate_skills.collect_errors(self.root)
        self.assertTrue(any("directory does not exist" in err for err in errors), errors)

    def test_frontmatter_name_must_match_directory(self):
        skill_dir = self.root / "skills" / "alpha-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: wrong-name\ndescription: Mismatched.\n---\n", encoding="utf-8"
        )
        write_manifest(self.root, [complete(["./skills/alpha-skill"])])
        errors = validate_skills.collect_errors(self.root)
        self.assertTrue(any("does not match directory name" in err for err in errors), errors)


class RealRepositoryTest(unittest.TestCase):
    def test_repository_passes_validation(self):
        self.assertEqual(validate_skills.collect_errors(REPO_ROOT), [])


if __name__ == "__main__":
    unittest.main()
