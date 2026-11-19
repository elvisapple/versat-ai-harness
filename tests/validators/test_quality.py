"""Exercise the quality entry point against real disposable Git repositories."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
QUALITY = ROOT / "scripts/validate/quality.sh"
ORIGINAL = "# Changelog\n\n## [Unreleased]\n\n- Existing entry.\n\n## [1.0.0]\n\n- Historical entry.\n"
NOTE = ORIGINAL.replace("- Existing entry.", "- Existing entry.\n- New behavior.")


class QualityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.git("init", "-q", "-b", "main")
        self.write("CHANGELOG.md", ORIGINAL)
        shutil.copyfile(ROOT / "ruff.toml", self.root / "ruff.toml")
        self.write("src/app.py", "value = 1\n")
        self.write("src/legacy.py", "import os\n\nx=  10\n")
        self.base = self.commit("Baseline")

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.root), *args], text=True
        ).strip()

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(exist_ok=True, parents=True)
        target.write_text(content, encoding="utf-8")
        return target

    def commit(self, subject):
        self.git("add", "-A")
        self.git(
            "-c",
            "user.name=Synthetic",
            "-c",
            "user.email=fixture@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "commit",
            "-qm",
            subject,
        )
        return self.git("rev-parse", "HEAD")

    def run_quality(self, *args, python=sys.executable, event=""):
        return subprocess.run(
            ["bash", str(QUALITY), "--root", str(self.root), *args],
            env={**os.environ, "PYTHON": python, "GITHUB_EVENT_NAME": event},
            capture_output=True,
            text=True,
        )

    def check(self, base=None):
        return self.run_quality("--base", base or self.base)

    def check_event(self, event, payload):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "event.json"
            path.write_text(json.dumps(payload))
            return self.run_quality("--github-event", str(path), event=event)

    def assert_pass(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_fail(self, result, expected):
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(expected, result.stdout + result.stderr)

    def test_new_note_and_clean_changed_file_skip_unrelated_legacy(self):
        self.write("src/app.py", "value = 2\n")
        self.write("CHANGELOG.md", NOTE)
        result = self.check()
        self.assert_pass(result)
        self.assertIn("checking 1 changed Python source", result.stdout)
        self.assertNotIn("legacy.py", result.stdout)

    def test_missing_duplicate_moved_and_historical_only_notes_fail(self):
        self.write("src/app.py", "value = 2\n")
        for content in (
            ORIGINAL,
            ORIGINAL.replace("Existing entry.", "Existing entry.\n* existing  entry."),
            ORIGINAL.replace("- Historical entry.\n", "").replace(
                "- Existing entry.", "- Existing entry.\n- Historical entry."
            ),
            ORIGINAL.replace("Historical entry.", "Changed historical entry."),
        ):
            with self.subTest(content=content):
                self.write("CHANGELOG.md", content)
                self.assert_fail(self.check(), "Add a new entry")

    def test_ambiguous_unreleased_or_fenced_example_does_not_pass(self):
        self.write("src/app.py", "value = 2\n")
        self.write("CHANGELOG.md", NOTE + "\n## [Unreleased] ##\n")
        self.assert_fail(self.check(), "exactly one")
        self.write(
            "CHANGELOG.md",
            ORIGINAL.replace("- Existing entry.", "```text\n- Example entry.\n```"),
        )
        self.assert_fail(self.check(), "Add a new entry")

    def test_exemption_empty_diff_and_mixed_paths(self):
        self.assert_pass(self.check())
        self.write("specs/changes/fixture/proposal.md", "# Draft\n")
        self.git("add", "specs")
        self.assertIn("Changelog: exempt", self.check().stdout)
        self.write(".github/workflows/changed.yml", "name: Changed\n")
        self.git("add", ".github")
        self.assert_fail(self.check(), "Add a new entry")

    def test_initial_changelog_after_absent_base_file(self):
        self.git("rm", "CHANGELOG.md")
        baseline = self.commit("Remove baseline changelog")
        self.write("CHANGELOG.md", NOTE)
        self.write("src/app.py", "value = 2\n")
        self.assert_fail(self.check(baseline), "Add a new entry")
        self.git("add", "CHANGELOG.md")
        self.assert_pass(self.check(baseline))

    def test_rename_checks_both_paths_and_deleted_python_is_not_linted(self):
        (self.root / "tests").mkdir()
        self.git("mv", "src/app.py", "tests/moved.py")
        (self.root / "src/legacy.py").unlink()
        self.assert_fail(self.check(), "Add a new entry")
        self.write("CHANGELOG.md", NOTE)
        result = self.check()
        self.assert_pass(result)
        self.assertIn("checking 1 changed Python source", result.stdout)

    def test_lint_and_format_fail_without_rewriting_and_history_is_required(self):
        source = self.write("src/app.py", "import os\n\nvalue=2\n")
        self.write("CHANGELOG.md", NOTE)
        result = self.check()
        self.assert_fail(result, "F401")
        self.assertIn("Would reformat", result.stdout + result.stderr)
        self.assertEqual(source.read_text(), "import os\n\nvalue=2\n")
        self.assert_fail(self.check("unknown-base"), "Fetch the required Git history")

    def test_symlink_is_rejected_and_missing_ruff_has_install_hint(self):
        self.write("CHANGELOG.md", NOTE)
        self.write("src/fake.py", "").unlink()
        (self.root / "src/fake.py").symlink_to("app.py")
        self.git("add", "src/fake.py")
        self.assert_fail(self.check(), "Symlink")
        with tempfile.TemporaryDirectory() as folder:
            python = Path(folder) / "python"
            subprocess.run(
                [sys.executable, "-m", "venv", "--without-pip", folder], check=True
            )
            python = python.parent / "bin/python"
            self.assert_fail(
                self.run_quality("--base", self.base, python=str(python)),
                "Install Ruff 0.14.14",
            )

    def test_push_and_new_branch_use_event_base(self):
        self.git("update-ref", "refs/remotes/origin/main", self.base)
        self.git("checkout", "-qb", "feature")
        self.write("src/app.py", "value = 2\n")
        self.write("CHANGELOG.md", NOTE)
        after = self.commit("Feature")
        event = {
            "ref": "refs/heads/feature",
            "before": self.base,
            "after": after,
            "repository": {"default_branch": "main"},
        }
        self.assert_pass(self.check_event("push", event))
        event.update(before="0" * 40, created=True)
        self.assert_pass(self.check_event("push", event))
        self.git("update-ref", "-d", "refs/remotes/origin/main")
        self.assert_fail(
            self.check_event("push", event), "Fetch the required Git history"
        )
        self.git("update-ref", "refs/remotes/origin/main", self.base)
        self.git("checkout", "-qb", "unchanged", self.base)
        event.update(ref="refs/heads/unchanged", after=self.base)
        self.assert_pass(self.check_event("push", event))

    def test_initial_root_push_checks_complete_tree(self):
        event = {
            "ref": "refs/heads/main",
            "before": "0" * 40,
            "after": self.base,
            "created": True,
            "repository": {"default_branch": "main"},
        }
        self.assert_fail(self.check_event("push", event), "F401")

    def test_pr_compares_the_merge_result_to_the_event_base(self):
        self.git("checkout", "-qb", "feature")
        self.write("src/app.py", "value = 2\n")
        self.write("CHANGELOG.md", NOTE)
        head = self.commit("Feature")
        event = {"pull_request": {"base": {"sha": self.base}, "head": {"sha": head}}}
        self.assert_fail(self.check_event("pull_request", event), "PR merge revision")
        self.git("checkout", "-q", "main")
        self.git(
            "-c",
            "user.name=Synthetic",
            "-c",
            "user.email=fixture@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "merge",
            "--no-ff",
            "-qm",
            "PR merge",
            "feature",
        )
        self.assert_pass(self.check_event("pull_request", event))
