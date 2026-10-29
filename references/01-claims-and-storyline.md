# Claims, storyline, evidence gates

## Claim ledger (do this before any prose)
One row per claim: object | metric | denominator | split | seed(s) | protocol | evidence path | level. Levels: **R** registered/confirmatory, **S** supporting, **D** descriptive. A claim with no row is not written. An experiment that serves no claim is moved to the supplement or dropped.

## Storyline chain (one sentence each; every section's hook is the next link)
default assumption -> observable failure (counter-intuitive, quantified) -> mechanism diagnosis -> design principle -> falsifiable prediction -> diagnostic experiment -> task result under a registered protocol -> claim boundary -> what the community should do differently.
Write the whole chain as one sentence and check that abstract, intro and conclusion tell the same chain.

## Evidence gates for strong words
| Word | Needs |
|---|---|
| repairs / restores / improves | paired test with interval on a held-out or fresh split, protocol stated |
| generalises | the second setting was not used in development |
| outperforms / best | same benchmark, same protocol, published or equally tuned baselines |
| mechanism / because | an intervention or a prediction that could have failed, not only a correlation |
| robust | named shifts, each with its own result |
Weaker word until the gate passes. Task success alone is not mechanism evidence; real-robot results show feasibility, not mechanism.

## Claim wording
A claim is "a scoped result of a defined method under a defined protocol". Use scope phrases that carry information ("on <benchmark> with <N> fresh layouts"), not hedges ("somewhat", "to some extent"). Write "no clear difference" when intervals overlap zero; do not call a tie a win.

## Before writing
Draw the failure figure first. Separate development from confirmation. Write down a prediction for every design component that could fail. Simulate a reviewer: if a conclusion needs experiments you do not have, downgrade the wording or leave a TODO; do not paper over it.
