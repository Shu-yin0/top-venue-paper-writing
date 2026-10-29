# Provenance and how far to trust the rules

## Where the rules come from
The checklists were distilled from an in-house 11-point writing handbook (abstract, introduction, related work, method, experiments, limitations, conclusion, whole paper and de-AI pass, title, figures and tables, supplement). The handbook in turn collects convergent advice from published writing guides, reviewer guidelines and close readings of well-received papers, and keeps the points of disagreement. Two empirical-ML papers in the robot-learning area were written and audited with it; the lessons that generalised are in `01` and `08`.

The paragraph above records provenance supplied in the original v1.0.0 archive. The underlying private handbook and paper-level outcomes are not included here and have not been independently verified as part of this repository's packaging. Treat these guides as practical heuristics, not validated evidence of improved acceptance rates.

## What kind of rules these are
- **Rules of thumb with defaults.** Word budgets (abstract 140-200, conclusion 100-150, limitations 3 +/- 1 items) are defaults for a typical 8-page vision/ML paper. The venue's call for papers always wins: page limit, external-link rule, anonymity, code and compute-report policy, supplement deadline.
- **Order of authority when rules clash:** venue rules > the authors' explicit instruction for this paper > this skill.
- **Heuristics, not detectors.** The word lists in `scripts/paperlint.py` and the "AI fingerprint" advice in `08` point to places to look. A listed word with a reason can stay; a clean grep does not make a paragraph good.
- **Do not copy sentences.** Templates keep the functional slot (what the sentence does), never the wording. Quoted example titles or abstracts from other papers are for study, not for reuse.
- **Citations.** Any reference you add is checked against a primary source (arXiv page, publisher, proceedings) first. An invented or mismatched entry can be a desk reject. Award or "best paper" status is cited only after checking the official page.

## Known gaps
No rule here replaces a cold read by someone outside the project. Run one before submission (give them the title, abstract, Figure 1 and conclusion; ask only "what is the claim, and where do you not believe it?").
