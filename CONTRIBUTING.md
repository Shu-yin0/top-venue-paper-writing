# Contributing

Small, evidence-backed improvements are welcome: clearer writing guidance, realistic synthetic examples, or reproducible linter fixes.

1. Describe the manuscript problem or command behavior being improved.
2. Keep reusable guidance in the relevant reference; keep `SKILL.md` focused on routing.
3. Mark invented examples as synthetic. Do not upload unpublished manuscripts, identities from anonymous submissions, or confidential results.
4. For script changes, include a regression test that checks observable behavior.
5. Run `python -m unittest discover -s tests -v` and `python scripts/validate_skill.py`.
6. Update both READMEs if installation or public behavior changes.

The linter has no third-party runtime dependencies and supports Python 3.8+. Word-list additions should explain why the phrase merits review, without treating vocabulary as proof of AI authorship. Keep source attribution and the MIT license intact.
