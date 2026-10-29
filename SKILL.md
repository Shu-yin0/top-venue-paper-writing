---
name: top-venue-paper-writing
description: Draft, rewrite or audit empirical ML papers for CVPR, ICCV, ICLR and NeurIPS-style venues. Use for evidence-backed claims, section editing, whole-paper review and submission writing checks in English or Chinese.
---

# Top-venue paper writing

A working method for empirical ML papers: a claim ledger first, then section checklists with templates, then a whole-paper pass and scripted submission checks. English or Chinese text; the rules do not depend on the language. Provenance and how far to trust the rules: `references/sources-and-evidence.md`.

## Pick a mode

| Mode | When | Steps |
|---|---|---|
| **Draft** | results exist, no text yet | ledger -> figures -> experiments -> intro -> method -> related work -> conclusion -> limitations -> abstract -> title -> supplement |
| **Audit** | a draft exists | ledger of what the draft claims -> one section audit per section (`templates/section-audit.md`) -> whole-paper pass -> change log |
| **Rewrite one section** | a single section is weak | open only that reference file, tick the checklist, rewrite, run the self-tests there |
| **Submission pass** | days before the deadline | `references/09-supplement-and-submission.md`, then the scripted checks below, then a cold read (`templates/cold-read-brief.md`) |

Abstract and title come last because they compress what the rest can prove.

## Working scope

Follow the user's requested scope. For a single-section edit, use the supplied claims and evidence and open only that section's guide; request missing context only when it affects the result. The full ledger and full-paper passes below apply to drafting or auditing a whole manuscript. Do not run experiments, upload a manuscript, or submit a paper as part of this skill.

Resolve paths to scripts and references relative to this skill's directory; manuscript paths refer to the user's project. Preserve the requested language and format. Return the requested text or audit plus consequential evidence gaps and unresolved author decisions, without requiring unnecessary artifact files.

## Workflow
1. **Build the claim ledger first** (`references/01-claims-and-storyline.md`, `templates/claim-ledger.md`). Ground substantive empirical claims in an object, metric, denominator, protocol and evidence path. Mark unavailable evidence explicitly; do not invent it.
2. For each section open only its reference file, tick the checklist, fix failures on the spot, and log each change as `rule -> file:line -> what changed` (`templates/change-log.md`).
3. Put every result you are unsure about on the open-decisions list (`templates/open-decisions.md`), not in the paper.
4. Finish with the whole-paper pass (`references/08-whole-paper-and-de-ai.md`) and the submission checks (`references/09-supplement-and-submission.md`).

| Section | Reference |
|---|---|
| Claims, storyline, evidence gates | `references/01-claims-and-storyline.md` |
| Title, abstract | `references/02-title-and-abstract.md` |
| Introduction | `references/03-introduction.md` |
| Related work | `references/04-related-work.md` |
| Method | `references/05-method.md` |
| Experiments | `references/06-experiments.md` |
| Figures and tables | `references/07-figures-and-tables.md` |
| Limitations, conclusion | `references/07b-limitations-and-conclusion.md` |
| Whole paper, de-AI | `references/08-whole-paper-and-de-ai.md` |
| Supplement, packaging, final checks | `references/09-supplement-and-submission.md` |
| Provenance, limits of the rules | `references/sources-and-evidence.md` |
| Worked before/after rewrites (synthetic) | `examples/rewrites.md` |

## Scripted checks (`scripts/paperlint.py`, stdlib only)
```
python3 scripts/paperlint.py length  main.tex                         # abstract / conclusion word budgets
python3 scripts/paperlint.py words   main.tex --lists ai,risk,hedge   # AI fingerprints, evidence-gated words, hedges
python3 scripts/paperlint.py overlap main.tex main.tex --part-a abstract --part-b conclusion   # runs of 8 identical words
python3 scripts/paperlint.py suppmap main.tex supp.tex                # every supplement section referenced from the main text
python3 scripts/paperlint.py anon    submission.zip --patterns names.txt   # paths, emails, hostnames, URLs, PDF metadata
```
Hits are prompts to look, not verdicts. Exit status 0 means no findings, 1 means findings, and 2 means invalid input or a command error. The checks can go into a Makefile. Word-count and vocabulary checks target English source text; PDF anonymity scanning covers only basic literal metadata, not full PDF contents or images.

## Writing and evidence principles
- **The authors decide what enters the paper.** Keep every result in the internal ledger (negative ones too; nothing overwritten or deleted). For the paper and supplement, propose what to include; do not write a negative or ambiguous result in on your own. If the authors have not ruled on something, list it as an open decision. Do not omit material counterevidence or conditions in a way that makes a claim misleading; narrow or qualify that claim pending the decision.
- **Truthfulness floor.** Never write anything false. Narrow the claim instead of hiding a condition. "Outperforms", "solves", "state of the art", "first", "fully restores" need a same-protocol comparison or a test that supports them.
- **Launch, not work report.** Organise around the strongest valid advantages. No process narrative (what was tried, what failed, what was written after the results); remove vague hedges while preserving justified uncertainty; each caveat appears once, where it matters, as short as possible. This is a style rule, not permission to overstate: every claim still lands on a number, table or test.
- **Each fact once.** Text explains what a figure or table shows for the claim (claim -> which rows or panels carry it -> what that validates); it does not repeat the numbers. Only key conclusions repeat (abstract, contributions, conclusion).
- **Anonymity and housekeeping.** Double-blind packages contain no names, paths, hostnames, job ids or internal experiment codes. Internal ids never appear in paper text.
- **Venue rules win.** Page limits, link rules, code and compute-report policies of the current call override any default here.

## What this skill does not do
It does not run experiments, choose the research question or decide venue strategy. It does not invent citations: every reference is checked against a primary source before it is cited (a fake citation can be a desk reject).
