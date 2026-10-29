# Experiments

- Build the claim <-> experiment map first (claim | experiment | figure or table | statistics | level R/S/D). Experiments without a claim go to the supplement.
- Cover six kinds: main comparison, ablation, diagnosis (mechanism attribution), generalisation, negative or boundary results (selected by the author), efficiency.
- Baselines: retrained under the same budget or the differences stated. Shared references (one native baseline for several seeds) are stated as such. Primary tests are separated from exploratory ones; multiple-comparison correction is named once in the setup.
- Each subsection opens with the question it answers. Each paragraph: phenomenon -> explanation ("consistent with") -> evidence (number triple: value, comparison, interval) -> boundary.
- At most one headline number per paragraph, anchored to a comparison. Use at least four of the six number forms across the section: triple, difference, pattern shape, statistical care, boundary, cost.
- Main table: best in bold, a relative-difference column. Every figure has a takeaway sentence in the text.
- Self-tests: (1) cover the numbers - does the argument still read? (2) read only the first sentence of every paragraph - do they chain?
- Layout and cell counts, seeds and denominators are named; paired designs state the pairing key.

## Patterns and templates
Six ways to write a number: (1) triple: absolute -> relative gain -> baseline anchor ("41.2 mm, 30% lower than the strongest external baseline"); (2) difference form ("drops by only 6.8 pp, against 24.7 and 50.5 pp"); (3) law shape (fit + goodness + regime, "extrapolation untested"); (4) statistical care ("no clear difference between these pairs"); (5) boundary by absence ("without any task-specific training"); (6) efficiency with cost. Paragraph template: [phenomenon + figure pointer] -> [explanation, "consistent with" level] -> [evidence triple] -> [boundary: where it vanishes or fails].
Reading test: if covering all numbers leaves the argument standing, it is explanation-driven; if it collapses, it is number-stacking.
Fairness: baselines retrained under the same settings or the setting difference stated; several seeds sharing one reference are not independent replicates; report variance and hyper-parameter sensitivity, not a single best point; show development-set tuning and test-set-only main results. Do not treat task success as mechanism verification.
Anti-patterns: reading the table aloud, naked numbers without anchor or protocol, ablations that never tie to a mechanism, weak or untuned baselines, truncated axes.
