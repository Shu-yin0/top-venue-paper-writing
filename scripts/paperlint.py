#!/usr/bin/env python3
"""paperlint: small, dependency-free checks for a LaTeX/Markdown paper draft.

Subcommands (all stdlib, Python >= 3.8):

  words    FILE [--lists ai,risk,hedge] [--extra FILE]   banned / risky word scan, with line numbers
  length   FILE --part abstract|conclusion|all          word count against the checklist budget
  overlap  A B [--min 8]                                 runs of identical words shared by two texts
  anon     PATH [--patterns FILE] [--no-defaults]        anonymity scan of a directory, zip or PDF
  suppmap  MAIN.tex SUPP.tex                             main-text references vs supplement sections

Exit status: 0 for no findings, 1 for findings, 2 for invalid input or command errors.
The checks are heuristics: a hit is a prompt to look, not a verdict.
"""
import argparse
import io
import re
import sys
import zipfile
from pathlib import Path

# --------------------------------------------------------------------------- word lists

AI_WORDS = [
    "delve", "underscore", "multifaceted", "pivotal", "leverage", "foster", "nuanced",
    "poised", "unveil", "showcasing", "commendable", "intricate", "realm", "meticulous",
    "tapestry", "revolutionize", "revolutionise", "holistic", "moreover", "furthermore",
    "harness", "remarkably", "notably", "seamless", "seamlessly", "cutting-edge",
    "it is worth noting", "it is important to note", "in recent years",
    "attracted increasing attention", "has attracted", "paves the way", "pave the way",
    "plays a pivotal role", "plays a crucial role", "in conclusion", "a testament to",
]
# words that need an evidence gate (a test, a same-protocol comparison, a named shift)
RISK_WORDS = [
    "significantly", "significant", "outperforms", "outperform", "state-of-the-art",
    "sota", "solves", "solved", "first", "novel", "fully restores", "robust",
    "generalizes", "generalises", "zero-shot", "unified", "enables", "guarantee",
    "always", "never", "proves", "proof",
]
# hedges that weaken a claim without carrying information
HEDGE_WORDS = [
    "somewhat", "to some extent", "to a certain extent", "arguably", "seems to",
    "appears to", "may possibly", "in some sense", "relatively", "quite", "rather",
    "a bit", "fairly",
]
LISTS = {"ai": AI_WORDS, "risk": RISK_WORDS, "hedge": HEDGE_WORDS}


# --------------------------------------------------------------------------- text helpers

def read(path):
    return Path(path).read_text(encoding="utf-8", errors="replace")


def strip_tex_comments(s):
    out = []
    for line in s.splitlines():
        m = re.search(r"(?<!\\)%", line)
        out.append(line[: m.start()] if m else line)
    return "\n".join(out)


def tex_to_text(s):
    """Rough LaTeX -> prose: drop comments, citations/refs, environments markers, keep argument text."""
    s = strip_tex_comments(s)
    s = re.sub(r"\\(?:cite|citep|citet|ref|cref|Cref|eqref|label|autoref)\*?(?:\[[^\]]*\])*\{[^}]*\}", "", s)
    s = re.sub(r"\$[^$]*\$", " X ", s)
    s = re.sub(r"\\(?:begin|end)\{[^}]*\}", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", s)
    s = re.sub(r"[{}~]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def words_of(s):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.%]*", s)


def extract_part(tex, part):
    if part == "abstract":
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", strip_tex_comments(tex), re.S)
        if m:
            return m.group(1)
        m = re.search(r"^#+\s*Abstract\s*$(.*?)(?=^#+\s|\Z)", tex, re.S | re.M | re.I)
        return m.group(1) if m else None
    if part == "conclusion":
        t = strip_tex_comments(tex)
        m = re.search(r"\\section\*?\{[^}]*Conclusion[^}]*\}(.*?)(?=\\section|\\bibliography|\\end\{document\}|\Z)", t, re.S | re.I)
        if m:
            return m.group(1)
        m = re.search(r"^#+\s*Conclusions?\s*$(.*?)(?=^#+\s|\Z)", tex, re.S | re.M | re.I)
        return m.group(1) if m else None
    return tex


# --------------------------------------------------------------------------- words

def cmd_words(a):
    names = [n for n in a.lists.split(",") if n]
    vocab = []
    for n in names:
        if n not in LISTS:
            raise ValueError(f"unknown list {n!r}; choose from {', '.join(LISTS)}")
        vocab += [(w, n) for w in LISTS[n]]
    if a.extra:
        vocab += [(l.strip().lower(), "extra") for l in read(a.extra).splitlines() if l.strip() and not l.startswith("#")]
    text = read(a.file)
    lines = strip_tex_comments(text).splitlines()
    pats = [(re.compile(r"(?<![A-Za-z])" + re.escape(w) + r"(?![A-Za-z])", re.I), w, n) for w, n in vocab]
    hits = 0
    counts = {}
    for i, line in enumerate(lines, 1):
        for p, w, n in pats:
            for m in p.finditer(line):
                hits += 1
                counts[(n, w)] = counts.get((n, w), 0) + 1
                lo, hi = max(0, m.start() - 40), min(len(line), m.end() + 40)
                print(f"{a.file}:{i}: [{n}] {w!r}: ...{line[lo:hi].strip()}...")
    if counts:
        print("\nsummary:")
        for (n, w), c in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"  {c:3d}  [{n}] {w}")
    print(f"\n{hits} hit(s). 'risk' words need a test or comparison that supports them; 'ai' words need a reason to stay.")
    return 1 if hits else 0


# --------------------------------------------------------------------------- length

BUDGET = {"abstract": (140, 200), "conclusion": (100, 150)}


def cmd_length(a):
    tex = read(a.file)
    parts = ["abstract", "conclusion"] if a.part == "all" else [a.part]
    bad = 0
    for part in parts:
        seg = extract_part(tex, part)
        if seg is None:
            print(f"{part}: not found in {a.file}")
            bad += 1
            continue
        n = len(words_of(tex_to_text(seg)))
        lo, hi = BUDGET.get(part, (0, 10**9))
        ok = lo <= n <= hi
        bad += 0 if ok else 1
        print(f"{part}: {n} words (budget {lo}-{hi}) {'OK' if ok else 'OUT OF RANGE'}")
    return 1 if bad else 0


# --------------------------------------------------------------------------- overlap

def norm_words(s):
    return [w.lower() for w in words_of(tex_to_text(s))]


def cmd_overlap(a):
    ta, tb = read(a.a), read(a.b)
    for path, part, content in ((a.a, a.part_a, ta), (a.b, a.part_b, tb)):
        if part and extract_part(content, part) is None:
            raise ValueError(f"{part} not found in {path}")
    wa = norm_words(extract_part(ta, a.part_a) if a.part_a else ta)
    wb = norm_words(extract_part(tb, a.part_b) if a.part_b else tb)
    n = a.min
    grams = {}
    for i in range(len(wb) - n + 1):
        grams.setdefault(tuple(wb[i:i + n]), i)
    found, i = [], 0
    while i <= len(wa) - n:
        g = tuple(wa[i:i + n])
        if g in grams:
            j, k = i + n, grams[g] + n
            while j < len(wa) and k < len(wb) and wa[j] == wb[k]:
                j += 1
                k += 1
            found.append(" ".join(wa[i:j]))
            i = j
        else:
            i += 1
    for f in found:
        print(f"shared run ({len(f.split())} words): {f}")
    print(f"{len(found)} run(s) of >= {n} identical words.")
    return 1 if found else 0


# --------------------------------------------------------------------------- anon

DEFAULT_ANON = [
    (r"[A-Za-z]:[\\/]Users[\\/][A-Za-z0-9_.-]+", "home path"),
    (r"/home/[A-Za-z0-9_.-]+", "home path"),
    (r"/Users/[A-Za-z0-9_.-]+", "home path"),
    (r"/data/[A-Za-z0-9_.-]+", "data path"),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "email"),
    (r"https?://[^\s}\\)>\"']+", "URL (check venue rules)"),
    (r"\b(?:github|gitlab|huggingface|wandb|overleaf)\.(?:com|co|ai)\b", "hosting site"),
    (r"\b(?:sbatch|squeue|srun|slurm)\b", "scheduler word"),
    (r"\b(?:acknowledg(?:e|ement)s?|thanks to|funded by|grant no)\b", "acknowledgement"),
    (r"\bjob[ _-]?(?:id)?\s*#?\d{4,}\b", "job id"),
]
TEXT_SUFFIX = {".tex", ".bib", ".md", ".txt", ".py", ".sh", ".json", ".yaml", ".yml", ".cfg", ".csv"}
TEMPLATE_SUFFIX = {".sty", ".bst", ".cls"}  # venue files carry their own URLs and emails; skipped
BENIGN_URL = re.compile(r"https?://(?:www\.)?(?:arxiv\.org|doi\.org|openreview\.net|aclanthology\.org|proceedings\.mlr\.press)", re.I)


def scan_text(label, text, pats, out, is_bib=False):
    for i, line in enumerate(text.splitlines(), 1):
        for p, why in pats:
            m = p.search(line)
            if not m:
                continue
            if why.startswith("URL") and BENIGN_URL.match(m.group(0)):
                continue
            if is_bib and why in ("hosting site",) or (is_bib and why.startswith("URL")):
                continue  # code/model links in references are checked by hand against the venue's link rule
            out.append(f"{label}:{i}: [{why}] {m.group(0)[:80]}")


def scan_pdf_meta(label, raw, out):
    head = raw[:200000] + raw[-200000:]
    seen = set()
    for key in (b"/Author", b"/Title", b"/Subject", b"/Keywords"):
        for m in re.finditer(re.escape(key) + rb"\s*\(([^)]*)\)", head):
            val = m.group(1).decode("latin-1", "replace")
            if val.strip() and (key, val) not in seen:
                seen.add((key, val))
                out.append(f"{label}: PDF metadata {key.decode()} = {val[:80]!r} (check it names no one)")


def cmd_anon(a):
    pats = [] if a.no_defaults else [(re.compile(p, re.I), w) for p, w in DEFAULT_ANON]
    if a.patterns:
        for l in read(a.patterns).splitlines():
            l = l.strip()
            if l and not l.startswith("#"):
                pats.append((re.compile(re.escape(l), re.I), "your pattern"))
    out = []
    root = Path(a.path)
    if not root.exists():
        raise ValueError(f"Input path does not exist: {root}")
    if root.suffix.lower() == ".zip":
        with zipfile.ZipFile(root) as z:
            for info in z.infolist():
                if info.is_dir():
                    continue
                name = info.filename
                scan_text(f"{root.name}!{name}", name, pats, out)  # file names too
                raw = z.read(name)
                suf = Path(name).suffix.lower()
                if suf in TEXT_SUFFIX:
                    scan_text(f"{root.name}!{name}", raw.decode("utf-8", "replace"), pats, out, suf == ".bib")
                elif name.lower().endswith(".pdf"):
                    scan_pdf_meta(f"{root.name}!{name}", raw, out)
    else:
        files = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
        for p in files:
            scan_text(str(p), str(p), pats, out)
            if p.suffix.lower() in TEXT_SUFFIX:
                scan_text(str(p), read(p), pats, out, p.suffix.lower() == ".bib")
            elif p.suffix.lower() == ".pdf":
                scan_pdf_meta(str(p), p.read_bytes(), out)
    print("\n".join(out))
    print(f"{len(out)} finding(s). Also check by eye: figures with embedded text, comments in code, video, supplementary file names.")
    return 1 if out else 0


# --------------------------------------------------------------------------- suppmap

def cmd_suppmap(a):
    main, supp = strip_tex_comments(read(a.main)), strip_tex_comments(read(a.supp))
    n_sections = len(re.findall(r"\\section\{", supp))
    refs = {}
    for m in re.finditer(r"(?:Supp(?:lement(?:ary)?)?\.?|Sec\.|Section)[~\s]*S(\d+)(?:\.\d+)*", main):
        refs.setdefault(int(m.group(1)), 0)
        refs[int(m.group(1))] += 1
    missing = [i for i in range(1, n_sections + 1) if i not in refs]
    bogus = sorted(i for i in refs if i > n_sections or i < 1)
    print(f"supplement sections: {n_sections}; distinct top-level sections referenced from main: {len(refs)}")
    if missing:
        print("never referenced from the main text: " + ", ".join(f"S{i}" for i in missing))
    if bogus:
        print("references to sections that do not exist: " + ", ".join(f"S{i}" for i in bogus))
    if not missing and not bogus:
        print("every supplement section is referenced; no dangling reference.")
    return 1 if (missing or bogus) else 0


# --------------------------------------------------------------------------- main

def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("words")
    p.add_argument("file")
    p.add_argument("--lists", default="ai,risk,hedge")
    p.add_argument("--extra", help="file with one extra banned phrase per line")
    p.set_defaults(fn=cmd_words)

    p = sub.add_parser("length")
    p.add_argument("file")
    p.add_argument("--part", choices=["abstract", "conclusion", "all"], default="all")
    p.set_defaults(fn=cmd_length)

    p = sub.add_parser("overlap")
    p.add_argument("a")
    p.add_argument("b")
    p.add_argument("--min", type=positive_int, default=8)
    p.add_argument("--part-a", choices=["abstract", "conclusion"])
    p.add_argument("--part-b", choices=["abstract", "conclusion"])
    p.set_defaults(fn=cmd_overlap)

    p = sub.add_parser("anon")
    p.add_argument("path")
    p.add_argument("--patterns", help="file with one forbidden string per line (names, hostnames, lab words)")
    p.add_argument("--no-defaults", action="store_true")
    p.set_defaults(fn=cmd_anon)

    p = sub.add_parser("suppmap")
    p.add_argument("main")
    p.add_argument("supp")
    p.set_defaults(fn=cmd_suppmap)

    a = ap.parse_args()
    try:
        result = a.fn(a)
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
        ap.error(str(exc))
    sys.exit(result)


if __name__ == "__main__":
    main()
