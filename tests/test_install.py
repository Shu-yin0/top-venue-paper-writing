import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts/install.py"


class Installation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dest = Path(self.temp.name) / "skill"

    def run_install(self, *args, **kwargs):
        return subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8", timeout=15, **kwargs)

    def test_dry_run_writes_nothing(self):
        result = self.run_install("--dest", self.dest, "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.dest.exists())

    def test_install_includes_runtime_resources(self):
        result = self.run_install("--dest", self.dest)
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ("SKILL.md", "LICENSE", "agents/openai.yaml", "scripts/paperlint.py",
                     "references/06-experiments.md", "templates/claim-ledger.md", "assets/icon.svg"):
            self.assertTrue((self.dest / name).is_file(), name)
        self.assertFalse((self.dest / "tests").exists())
        self.assertFalse((self.dest / ".git").exists())
        demo = subprocess.run([sys.executable, "-X", "utf8", str(self.dest / "scripts/paperlint.py"),
                               "words", str(self.dest / "examples/demo-paper.tex"), "--lists", "ai,risk"],
                              capture_output=True, text=True, encoding="utf-8", timeout=15)
        self.assertEqual(demo.returncode, 1, demo.stderr)
        self.assertIn("2 hit(s)", demo.stdout)

    def test_existing_install_is_preserved(self):
        self.dest.mkdir()
        sentinel = self.dest / "keep.txt"
        sentinel.write_text("local edits", encoding="utf-8")
        result = self.run_install("--dest", self.dest)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "local edits")
        self.assertFalse((self.dest / "SKILL.md").exists())

    def test_codex_home_override(self):
        result = self.run_install("--agent", "codex", env={**os.environ, "CODEX_HOME": str(self.dest)})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.dest / "skills/top-venue-paper-writing/SKILL.md").is_file())

    def test_reject_recursive_installation(self):
        destination = ROOT / "nested-test-destination"
        result = self.run_install("--dest", destination, "--dry-run")
        self.assertEqual(result.returncode, 2)
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
