# Method

- First sentence of each component is a *why* sentence: because X fails, we replace it; or the component corresponds to a named challenge; or a distributional argument.
- One-to-one map between the challenges in the intro and the components here; no orphan component, no orphan challenge. No catalogue subsections.
- An overview figure exists; its caption is a mini abstract, never "Overview".
- Notation: one symbol, one meaning; no overloading; no triple subscripts; every displayed equation punctuated; number only the equations that are cited; macros for symbols; consistent label prefixes.
- Each loss term answers a failure mode named earlier. Deployment rules are given as a table or short pseudo-code (the box may live in the supplement).
- Terms are defined in the setup, not coined mid-text. Hyper-parameters are in the main text or at the start of the experiments. Method sections do not absorb experiment protocol; that moves to the setup.
- Reproduction triple: code, README, a minimal notebook or script, promised in the right place (anonymous archive for review; "will be released" is allowed, a link to a public repo is not).

## Patterns and templates
Four why-sentence patterns (component-first-sentence rewriters): Because-fails ("Because <failure> occurs under <condition>, we <design>"); replace ("We replace <default> with <substitute>, which <mechanism claim>"; falsifiable: undo the replacement and you are back at the baseline); naming correspondence (the design or loss reuses the failure's noun); distribution argument ("Deployment sees <shift>; training therefore perturbs <the same dimension>"). A component that cannot be rewritten into one of these is demoted to an implementation detail.
Notation ten: consistent symbols; no overloading; avoid triple subscripts; do not use "for any x" for a specific object; bold vectors uniformly; avoid look-alike pairs (u/upsilon); punctuate equations; number only cited equations; label prefixes eq/sec/fig + role; symbols via macros.
Skeleton: Setup and notation (term box, notation table) -> Method: overview (figure + a one-paragraph mechanism, isomorphic to the abstract's mechanism sentence) -> one subsection per component -> training objective (full loss, which term answers which failure, weights) -> deployment rule (table + pseudo-code) -> implementation details -> long tail to the supplement. The method figure's caption is the component's mini abstract. Component deletion test: remove any component's description; if the argument chain survives, the component does not belong. Method sections hold no results (cost numbers aside). Order by argument, not by the order the work happened.
