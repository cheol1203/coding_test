"""Integration checks using disposable repositories, never the real Git index."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parents[1]
UPDATER = PROJECT / "scripts/update_readme_stats.py"
INSTALLER = PROJECT / "scripts/install_hooks.py"
SAMPLE = """# My archive
<!-- stats:summary:start -->
old summary
<!-- stats:summary:end -->
<!-- stats:levels:start -->
old levels
<!-- stats:levels:end -->
<!-- stats:categories:start -->
old categories
<!-- stats:categories:end -->
## Manual records
| type | D2 | title | SWEA | <a href="./solutions/DP/SWEA_1_one.md">solution</a> | date | my comment | mark |
manual note
"""


class ReadmeStatsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".stats-test-", dir=PROJECT)
        self.root = Path(self.temp.name)
        self.addCleanup(self.cleanup_repository)
        self.env = os.environ.copy()
        for name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_PREFIX"):
            self.env.pop(name, None)
        self.git("init", "-q")
        self.git("config", "user.name", "Stats Test")
        self.git("config", "user.email", "stats-test@example.invalid")
        self.git("config", "core.autocrlf", "false")
        self.write("README.md", SAMPLE)
        self.write("solutions/DP/SWEA_1_one.md", "# One\n")

    def run_command(self, *args, check=True):
        result = subprocess.run(args, cwd=self.root, env=self.env, capture_output=True,
                                text=True, encoding="utf-8", errors="replace")
        if check:
            self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def cleanup_repository(self):
        self.assertEqual(self.root.resolve().parent, PROJECT)
        self.assertTrue(self.root.name.startswith(".stats-test-"))
        self.temp.cleanup()

    def git(self, *args):
        return self.run_command("git", *args).stdout

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def update(self, *args, check=True):
        return self.run_command(sys.executable, str(UPDATER), *args, check=check)

    def test_add_delete_and_unknown_difficulty_without_changing_manual_records(self):
        self.write("solutions/String/Programmers_2_two.md", "# Two\n")
        self.update()
        text = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertIn("<strong>2문제</strong>", text)
        self.assertIn("| SWEA | D2 | 1 |", text)
        self.assertIn("| 프로그래머스 | 미분류 | 1 |", text)
        self.assertEqual(text.split("## Manual records", 1)[1], SAMPLE.split("## Manual records", 1)[1])
        self.update()
        self.assertEqual((self.root / "README.md").read_text(encoding="utf-8"), text)
        (self.root / "solutions/DP/SWEA_1_one.md").unlink()
        self.update()
        text = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertIn("<strong>1문제</strong>", text)
        self.assertNotIn("| SWEA | D2 | 1 |", text)

    def test_staged_counts_ignore_untracked_files_and_preserve_unstaged_readme_edits(self):
        self.git("add", ".")
        self.write("solutions/String/Programmers_2_two.md", "# Not staged\n")
        self.write("README.md", SAMPLE + "not for this commit\n")
        self.update("--staged")
        staged = self.git("show", ":README.md")
        working = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertIn("<strong>1문제</strong>", staged)
        self.assertNotIn("not for this commit", staged)
        self.assertIn("not for this commit", working)
        self.assertIn("<strong>1문제</strong>", working)

    def test_missing_markers_fail_without_writing(self):
        self.write("README.md", "# No generated sections\n")
        result = self.update(check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("markers", result.stderr)
        self.assertEqual((self.root / "README.md").read_text(), "# No generated sections\n")

    def test_installed_hook_updates_readme_in_a_real_commit(self):
        scripts = self.root / "scripts"
        scripts.mkdir()
        shutil.copy2(UPDATER, scripts / UPDATER.name)
        shutil.copy2(INSTALLER, scripts / INSTALLER.name)
        self.run_command(sys.executable, str(scripts / INSTALLER.name))
        self.git("add", ".")
        self.git("commit", "-qm", "Test automatic stats")
        committed = self.git("show", "HEAD:README.md")
        self.assertIn("<strong>1문제</strong>", committed)
        self.assertNotIn("old summary", committed)
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_installer_preserves_an_existing_unrelated_hook(self):
        hook = self.root / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\necho existing\n", encoding="utf-8")
        result = self.run_command(sys.executable, str(INSTALLER), check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("existing pre-commit hook", result.stderr)
        self.assertEqual(hook.read_text(), "#!/bin/sh\necho existing\n")


if __name__ == "__main__":
    unittest.main()
