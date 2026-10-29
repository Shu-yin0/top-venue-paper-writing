# Claim ledger

One row per claim. A claim with no row is not written; an experiment that serves no claim goes to the supplement or is dropped.
Level: **R** registered/confirmatory, **S** supporting, **D** descriptive.

| id | claim (one sentence, scope words first) | object | metric | denominator | split / seeds | protocol and test | evidence path (file, table, figure) | level | where it appears (abs / intro / sec / concl) |
|---|---|---|---|---|---|---|---|---|---|
| C1 | On <benchmark> with <N> fresh layouts, <method> raises <metric> from <a> to <b> | model X | success rate | 150 layouts x 1 seed | fresh, never used in development | paired difference, 95% interval, Holm over 3 hypotheses | results/main.json -> Tab. 1 | R | abs, intro, 5.1, concl |
| C2 | | | | | | | | | |

Checks before prose: every number in the paper traces to a row; every strong word (see `references/01`) has its gate in the protocol column; abstract, intro and conclusion tell the same chain.
