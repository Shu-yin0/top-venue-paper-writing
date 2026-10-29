# Supplement and submission checks

## Supplement
- The core evidence is in the main text: with the supplement covered, a reviewer can still judge the paper.
- One topic per section, descriptive titles, mirror the order of the main text, start with a navigation page (contents plus one line per section), number S-sections in order of first reference.
- Every section is referenced at least once from the main text (script: extract `Supp.~S<d>` references and compare with section numbers). Numbers come from the same macros or result files as the main text. Level labels use the same vocabulary.
- Contents are positive or explanatory: derivations, protocols, full tables, extra analyses. No work-log content: no errata, "moved from main", pending markers, job ids, hostnames, superseded tables (if an old table must stay, label it SUPERSEDED). Whether any negative result enters is the author's decision.

## Final checks (run, do not eyeball)
- Build clean: page limit met (references start on a new page when the template allows), 0 undefined references, 0 overfull boxes that matter, no short last lines in captions and paragraphs, rendered pages looked at.
- Anonymity: grep for names, paths, hostnames, job ids, internal ids, URLs, and check PDF metadata, code comments and videos.
- Banned/risk words grep; AI-word grep (08); citations verified against primary sources; template and venue rules (page limits, external-link rules, code policy, compute-report policy) checked against the current call.
- Numbers: every number traced to a result file; spot-check random cells after each rebuild.
- Change log and handoff: record the change list (`rule -> file:line -> change`) and the open-decisions list for the author.

## Patterns and templates
- Four iron rules: reviewers are not obliged to read the supplement, so decisive evidence (main table, mechanism ablation, deciding controls) stays in the main text; support, do not repeat (one fact in one place, a pointer in the other); no results from improved methods obtained after the deadline; the supplement continues the paper, it is not a log.
- Goes in: full proofs and derivations; full implementation details (hyper-parameter tables, hardware, configs, reproduction notes); per-task or per-fold tables (the main text keeps pooled and representative rows); extra ablations and robustness promised by the main text ("see supplement"); qualitative results including failures, same protocol; metric definitions and statistical choices; data and licence details; video; code; concurrent-work list. Stays out: any evidence a reviewer needs to decide; partial results posing as complete; orphan sections.
- Numbering: S prefix for pages, sections, Figure S1 / Table S1 in order of first reference; one numbering unit per merged item (S1A/S1B go into S1); readable file names; the same template, notation and definitions as the main text; each section opens by pointing back to the main-text location ("This section extends Sec. 5.2").
- Video and code: the strongest result in the first ten seconds; narration beats silent video; anonymous inside frames; code with a README (three-step run, dependencies, seed notes) and a pointer from the matching supplement section.
- Supplement final checks share the main text's: AI-word grep, anonymity script, spelling (supplements have the highest error rate because they are checked least).
