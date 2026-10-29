# Before / after rewrites (synthetic examples)

All systems, numbers and domains below are made up to show the moves. Copy the move, not the sentence.

## Abstract opener
- Before: "In recent years, object detectors have attracted increasing attention and achieved remarkable performance."
- After: "Detectors fine-tuned for daytime scenes lose most of their accuracy at dusk, although only the lighting changes."
- Move: open on the concrete failure the reader can judge, drop the generic field-state sentence.

## Headline number (abstract S6)
- Before: "Our method significantly improves robustness."
- After: "Dusk accuracy rises from 31.4 to 62.8 mAP on 1,200 held-out scenes (paired 95% interval +29.9 to +33.0), with daytime accuracy unchanged within 0.4 mAP."
- Move: value, comparison, protocol, interval; no "significantly" without the test it names.

## Introduction niche (P2)
- Before: "However, existing methods have limitations."
- After: "Existing remedies retrain with night-time labels or add an enhancement network; whoever holds a released detector has neither."
- Move: the gap is specific (what is missing, for whom) and judgeable without technical background.

## Related-work paragraph
- Before: list of five methods, each "X proposes ...".
- After: "Domain-adaptation methods align features using target images [a,b]; test-time methods update normalisation statistics online [c,d]. Unlike both, our repair needs no target image and changes weights once."
- Move: group by relationship to the problem; end on the differentiating sentence.

## Method why-sentence
- Before: "We use a consistency loss."
- After: "Because the detector's day-time prediction is already correct on the same scene, we make it the target for every dusk rendering, instead of asking for new labels."
- Move: failure -> design -> mechanism claim, falsifiable by removing the loss.

## Experiment paragraph (phenomenon -> explanation -> evidence -> boundary)
- Before: "Table 2 shows that our method achieves the best results on all benchmarks."
- After: "The gain tracks how much each detector loses at dusk (Fig. 4): the three most brittle models recover 24.1, 22.7 and 19.9 mAP, the least brittle gains 1.3 (interval -0.6 to +3.1). It disappears when the shift is a lens artefact rather than lighting (Tab. 3, last row)."
- Move: one claim, anchored numbers, a pattern across models, a stated boundary.

## Figure caption
- Before: "Overview of our method."
- After: "A frozen detector supplies the target for its own dusk renderings. (a) Training uses day-night pairs of one scene. (b) The update is kept only if daytime accuracy holds. Blue = trained, grey = frozen; bars show 95% intervals."
- Move: claim sentence first, one sentence per panel, definitions last; a caption is a mini abstract.

## Limitation
- Before: "Our method fails on other tasks."
- After: "We evaluate driving scenes; extending to indoor robots would need a lighting model for artificial sources, which we leave to the next stage."
- Move: scope, consequence, next step; no self-negating subject.

## Conclusion
- Before: a shortened copy of the abstract with "In conclusion".
- After: "We showed that a released detector can repair its own dusk failure from its daytime predictions. Repair worked where the shift enters the network, not where it is most visible, and kept daytime accuracy. Teams that ship a detector can therefore audit and patch lighting failures without new labels; we next test sensor-level shifts."
- Move: past tense, one normative takeaway, one concrete next step, no run of 8 identical words with the abstract.
