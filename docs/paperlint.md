# paperlint CLI reference

Run from the repository root, or replace `scripts/paperlint.py` with its absolute path. Python 3.8+, standard library only. Inputs are read as UTF-8. Commands do not modify your manuscript.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | No findings from the selected heuristic |
| `1` | Findings to review |
| `2` | Invalid arguments, missing input, unreadable file or invalid ZIP |

A CI pipeline can fail on `1`; a human should decide whether the findings need edits.

## Word budgets

```bash
python scripts/paperlint.py length main.tex
python scripts/paperlint.py length draft.md --part abstract
```

Default budgets: abstract 140–200 words; conclusion 100–150 words. These are writing heuristics, not venue requirements. The parser recognizes LaTeX abstract environments and conclusion sections, or English Markdown headings `Abstract` and `Conclusion(s)`. It does not expand `\input`/`\include`, resolve macros, or count Chinese words reliably. A missing requested section is reported as a finding.

## Vocabulary review

```bash
python scripts/paperlint.py words main.tex --lists ai,risk,hedge
python scripts/paperlint.py words main.tex --lists risk --extra phrases.txt
```

`ai` means stock phrasing to review, not authorship detection. `risk` flags words that may need evidence; `hedge` flags vague qualifiers. Keep legitimate uses. Custom phrases are literal strings, one per line; lines beginning with `#` are comments. LaTeX comments are skipped; other source markup is not fully parsed.

## Repeated spans

```bash
python scripts/paperlint.py overlap main.tex main.tex --part-a abstract --part-b conclusion
python scripts/paperlint.py overlap abstract.md conclusion.md --min 10
```

Finds runs of at least eight matching words by default, after rough LaTeX normalization. `--min` must be positive. A requested section that does not exist is an input error; the tool does not silently substitute the entire manuscript. This is a repetition check, not a plagiarism detector.

## Supplement mapping

```bash
python scripts/paperlint.py suppmap main.tex supp.tex
```

Counts top-level `\section{...}` entries in the supplement and compares them with explicit references such as `Supp.~S1`, `Section S2` or `Sec. S3.2` in the main text. It assumes sequential S-numbering; it does not resolve `\ref{...}`, starred sections, custom macros or included files. Use only when your source follows that convention.

## Anonymity clues

```bash
python scripts/paperlint.py anon submission.zip
python scripts/paperlint.py anon submission-folder --patterns names.txt
python scripts/paperlint.py anon submission-folder --patterns names.txt --no-defaults
```

Supply a file, directory or ZIP. `names.txt` contains your own literal names, institutions or hostnames to search for, one per line; keep this private. Default patterns include home-directory paths, email addresses, hosting links, scheduler terms and acknowledgement phrases. Venue template files are not scanned as manuscript text. Bibliography URLs receive special treatment to reduce noise.

**Coverage is deliberately limited.** PDF inspection only looks for simple literal metadata fields in the beginning/end of the raw file. It does not parse compressed objects, XMP, visible PDF text, screenshots, embedded images or videos. Figures and the final rendered submission require manual review. URL exemptions are heuristics, not an authoritative interpretation of a venue's anonymity policy.
