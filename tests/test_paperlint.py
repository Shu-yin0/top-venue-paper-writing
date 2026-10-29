import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "paperlint.py"


def tex(a, c):
    return TEX.replace("@A@", a).replace("@C@", c)


def run(*args):
    p = subprocess.run([sys.executable, "-X", "utf8", "-s", "-I", str(SCRIPT), *map(str, args)], capture_output=True, text=True, encoding="utf-8", timeout=15)
    return p.returncode, p.stdout + p.stderr


TEX = r"""
\begin{abstract}
@A@
\end{abstract}
\section{Introduction}
We leverage a pivotal idea. % delve is in a comment
\section{Conclusion}
@C@
\section{References}
"""


class Lint(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.d = Path(self.temp.name)

    def write(self, name, text):
        p = self.d / name
        p.write_text(text, encoding="utf-8")
        return p

    def test_length_in_range(self):
        t = self.write("a.tex", tex(" ".join(["word"] * 150), " ".join(["term"] * 120)))
        rc, out = run("length", t)
        self.assertEqual(rc, 0, out)
        self.assertIn("abstract: 150 words", out)

    def test_length_out_of_range(self):
        t = self.write("a.tex", tex(" ".join(["word"] * 50), " ".join(["term"] * 120)))
        rc, out = run("length", t)
        self.assertEqual(rc, 1)
        self.assertIn("OUT OF RANGE", out)

    def test_words_ignores_comments(self):
        t = self.write("a.tex", tex("plain text", "plain text"))
        rc, out = run("words", t, "--lists", "ai")
        self.assertEqual(rc, 1)
        self.assertIn("leverage", out)
        self.assertIn("pivotal", out)
        self.assertNotIn("delve", out)

    def test_overlap(self):
        shared = "the quick brown fox jumps over the lazy dog today"
        t = self.write("a.tex", tex(shared + " and more", "unrelated start " + shared))
        rc, out = run("overlap", t, t, "--part-a", "abstract", "--part-b", "conclusion")
        self.assertEqual(rc, 1)
        self.assertIn("quick brown fox", out)

    def test_suppmap(self):
        main = self.write("m.tex", "see Supp.~S1 and Supp.~S3.2 and Supp.~S9")
        supp = self.write("s.tex", r"\section{A}\section{B}\section{C}")
        rc, out = run("suppmap", main, supp)
        self.assertEqual(rc, 1)
        self.assertIn("S2", out)
        self.assertIn("S9", out)

    def test_overlap_requires_positive_length(self):
        t = self.write("a.tex", tex("a short sentence", "another sentence"))
        for length in ("0", "-1"):
            rc, out = run("overlap", t, t, "--min", length)
            self.assertEqual(rc, 2, out)
            self.assertIn("positive integer", out)

    def test_overlap_missing_part_is_error(self):
        t = self.write("a.tex", "plain text without sections")
        rc, out = run("overlap", t, t, "--part-a", "abstract")
        self.assertEqual(rc, 2, out)
        self.assertIn("abstract not found", out)

    def test_missing_anon_input_is_error(self):
        rc, out = run("anon", self.d / "missing")
        self.assertEqual(rc, 2, out)
        self.assertIn("does not exist", out)

    def test_bad_zip_is_error(self):
        t = self.write("bad.zip", "not a zip")
        rc, out = run("anon", t)
        self.assertEqual(rc, 2, out)
        self.assertNotIn("Traceback", out)

    def test_unknown_word_list_is_error(self):
        t = self.write("a.tex", "text")
        rc, out = run("words", t, "--lists", "invalid")
        self.assertEqual(rc, 2, out)

    def test_windows_home_path(self):
        t = self.write("a.tex", r"Saved at C:\Users\alice\research")
        rc, out = run("anon", t)
        self.assertEqual(rc, 1, out)
        self.assertIn("home path", out)

    def test_utf8_custom_anonymity_pattern(self):
        t = self.write("a.tex", "机构名称：示例实验室")
        patterns = self.write("names.txt", "示例实验室")
        rc, out = run("anon", t, "--patterns", patterns, "--no-defaults")
        self.assertEqual(rc, 1, out)
        self.assertIn("your pattern", out)

    def test_anon_zip(self):
        z = self.d / "pkg.zip"
        with zipfile.ZipFile(z, "w") as f:
            f.writestr("main.tex", "path /home/alice/proj and mail bob@uni.edu")
            f.writestr("refs.bib", "url = {https://arxiv.org/abs/2601.00001}")
        rc, out = run("anon", z)
        self.assertEqual(rc, 1)
        self.assertIn("home path", out)
        self.assertIn("email", out)
        self.assertNotIn("arxiv", out)


if __name__ == "__main__":
    unittest.main()
