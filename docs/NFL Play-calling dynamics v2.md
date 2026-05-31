# Play-calling dynamics (NFL offensive and defensive systems) — dissipative Rosetta column

**NESS framing:** drive = repeated possessions supplied by clock, field position, downs, player energy, and opponent actions; sink = turnovers, punts, scores, clock expiration, and fatigue. The steady state is not a single drive but the **ongoing possession-exchange process** across a game and season.

**Schools-of-thought preamble** (§6½ B): NFL play-calling sits at the intersection of several partially competing traditions: classical coaching heuristics, game-theoretic mixed-strategy analysis, dynamic-programming/expected-points analytics, and newer learning/adaptation frameworks. The strongest consensus exists around small "peanut" models (fourth-down decision models, mixed-strategy run/pass balance, possession-value models). Disagreement is usually about *causal interpretation* and implementation, not the existence of the regularities themselves. Rows anchored on a single school's preferred explanation are graded loose even when the underlying regularity is widely accepted.

**Peanuts** (§6½ A):

* Fourth-down dynamic-programming possession-value models (Romer 2002). ([NBER][1])
* Run/pass mixed-strategy and serial-correlation analyses. ([ScienceDirect][2])
* Evolutionary-game / replicator dynamics as the accepted dynamical version of strategic adaptation. ([PMC][3])

## Table

| phenomenon (A)                                                                                                                 | established dissipative home + citation (B)                                                                                                          | character primitive [anchor] (C)                             | grade    |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------- |
| Offensive tendency adaptation (offense and defense adjusting frequencies over time)                                            | Evolutionary-game / replicator dynamics; strategy frequencies evolve according to relative payoff. ([PMC][3])                                        | deformation generators [DEFORMATION GENERATORS]              | S, tight |
| Emergence of a stable run/pass mix                                                                                             | Mixed-strategy game-theoretic adaptation; frequencies converge toward dynamically stable mixtures under payoff feedback. ([PMC][3])                  | c/s/r trichotomy [§14 / three-regime threshold]              | S, loose |
| Coordinators settling into distinct offensive identities ("run-heavy", "balanced", "pass-heavy") with occasional abrupt shifts | Multiple attractors and bistability in adaptive game dynamics. ([PubMed][4])                                                                         | metastable basins [§14 attractors]                           | S, loose |
| League-wide evolution of offensive systems (West Coast → spread → RPO families, etc.) across scales                            | Higher-order adaptive game dynamics and strategy evolution acting on slower timescales than individual plays. ([ScienceDirect][5])                   | platformed topology / RG type-identity [§6.5]                | S, loose |
| Possession-value models (field position and downs compressed into expected future value)                                       | Dynamic-programming state aggregation; many fast play outcomes summarized by slower possession-value variables. ([NBER][1])                          | heat-tax tower / plateau ladder [COMPRESSION]                | S, tight |
| Breakdown of pre-game game plans under extreme game states (garbage time, desperation, end-game chaos)                         | Effective possession-value models lose predictive power outside their normal operating regime. ([NBER][1])                                           | the Wall / loss of normal hyperbolicity [COMPRESSION / Wall] | S, loose |
| NFL play-calling ecosystem as a whole                                                                                          | Continuous throughput of possessions, information, adaptation, and resource expenditure; strategies decay if the competitive environment is removed. | substrate-is-NESS [POSITS]                                   | S, loose |

## What this surfaces

* **Within-field collapse:** Many apparently distinct coaching phenomena (offensive identity, coordinator philosophy, tendency adaptation, scheme evolution) collapse onto a common language of adaptive dynamical systems and attractors rather than isolated tactical choices.
* **The mint/supplied cut:** The cleanest version is not a specific play call but a *scheme identity*. A coordinator may "mint" a structural preference (which branch of strategy space they occupy), but its effectiveness/amplitude is supplied by personnel quality, opponent response, field position, and possession opportunities. Remove those drives and the observed advantage decays.
* **Most striking re-reading:** The strongest row is probably possession-value modeling → heat-tax tower. Modern expected-points frameworks are literally a coarse-graining operation: many fast play-level events are compressed into slower state variables.

## Honest scope

* Tightest rows: possession-value models → heat-tax tower; adaptive strategy evolution → deformation generators.
* Most other rows are **loose** because the NFL literature usually studies optimization, learning, or game-theoretic adaptation rather than explicitly dissipative physics.
* No row is character-grade (`C`). This is entirely an imported structural reading.
* No claim is made that MPA explains football. The column only re-reads existing dynamical treatments in a common coordinate system.

## Flagged for review (NOT table rows)

### Gaps

* Defensive/offensive "momentum" narratives: widely discussed, weak consensus on a dissipative home.
* Scripted-opening-drive effects: interesting candidate, but no clear dissipative treatment identified.

### Unidentified-drive (§6½ C)

* "Culture" or "identity" explanations for sustained offensive success when no throughput variable is specified.
* Claims that organizations "self-sustain" strategic advantages without identifying talent, information, or possession-flow inputs.

### Over-claim risks

* **Football drive → reservoir/release register.** The procedure's rejection example is correct: most literature models drives as terminating or absorbing processes, not sustained recharge/discharge systems. A direct reservoir/release mapping is unsafe. ([NBER][1])
* **Run/pass alternation → k_frust.** Negative serial correlation is empirically observed, but N=2 alternation is not a protected circulation under the procedure's discriminator. ([ScienceDirect][2])
* **Fourth-down go/kick → ignition.** Dynamic-programming decision boundaries are optimization thresholds, not bifurcations of a flow. ([NBER][1])
* **NFL play-calling as chirality/topological-bit.** No clean handedness or gauge-irremovable sign structure was found; forcing one would violate the import-only rule.

**Flag ratio:** 7 rows : 6 flags. For a handle-with-care field, that ratio is itself informative: the strongest structure appears in adaptation and coarse-graining, while several tempting football analytics concepts fail the dissipative-home authenticity gate.

---

## ADJUDICATION (integrator audit, 2026-05-31) — v2 vs v1, feedback into procedure + engine

**Verdict: real improvement, loop validated — and it confirms the deeper pattern (the over-map jumps one level up after each gate). No engine edit; two procedure gates landed.**

**What the v1→v2 hardening achieved:** all three v1 `tight` over-maps (drive→reservoir, alternation→k_frust, 4th-down→ignition) are now correctly in §6-FLAG over-claim risks, each citing the discriminator that rejects it; the chirality/topological-bit row was *declined* ("forcing one would violate import-only") — the discipline working. v1 mis-anchored on the static serial-correlation sub-literature; v2 found the genuine *dynamical* home (replicator/evolutionary-game dynamics, Hofbauer–Sigmund — real). The authenticity gate + N≥3 rule were internalized.

**The new slip the gates didn't yet catch (now gated):** Row 1 "strategy adaptation → **deformation generators**, `tight`." Deformation generators is an *advanced* primitive whose signature is an explicit Jacobian eigen-decomposition (damping⊕chirality⊕splitting); the NFL literature does not linearize a play-calling flow and read that off. "Has adaptation" was mapped to the most sophisticated-sounding primitive. Honest home for replicator-converging-to-a-stable-mix is **c/s/r / ignition**. Same root as v1 (reach exceeding the home), new costume: v1 over-reached on *structure*, v2 on *primitive sophistication*.

**The missed prize (engine-relevant lead, not an edit):** v2 *had* the replicator citation and routed it to the wrong primitive. Replicator dynamics over **≥3 mutually-countering play archetypes** is N≥3 cyclic dominance = RPS/May-Leonard = the framework's k_frust flagship. Routed correctly, this is **k_frust in strategy space** — the cross-column collapse (behavioral ⟷ ecological ⟷ Central Commitment). NFL was chosen for its data richness — which is exactly what could make a correctly-anchored ≥3-archetype version a candidate **`C`-grade behavioral instance** of the Central Commitment. Frontier/applications lead; does not auto-land.

**Engine:** no extension (confirmations + a lead, not a claim change). **Procedure refinements landed in `dissipative_rosetta_procedure.md`:** (i) §1 **advanced-primitive guard** (deformation generators / two frames need the field to *literally* supply the structure, not just "have dynamics/feedback"); (ii) §4 **grade-ceiling rule** (`tight` requires the col-B home to supply the chosen primitive's own signature, not merely *a* model); (iii) §8c worked-rejection (the deformation-generators slip) + the banked missed-collapse lesson (the over-map re-appears one level up; chase the ≥3-strategy k_frust collapse).

[1]: https://www.nber.org/papers/w9024?utm_source=chatgpt.com "It's Fourth Down and What Does the Bellman Equation Say? A Dynamic Programming Analysis of Football Strategy | NBER"
[2]: https://www.sciencedirect.com/science/article/pii/S2214804317300071?utm_source=chatgpt.com "Serial correlation in National Football League play calling and its effects on outcomes - ScienceDirect"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4113915/?utm_source=chatgpt.com "The replicator equation and other game dynamics - PMC"
[4]: https://pubmed.ncbi.nlm.nih.gov/26232971/?utm_source=chatgpt.com "Evolutionary game dynamics of controlled and automatic decision-making - PubMed"
[5]: https://www.sciencedirect.com/science/article/abs/pii/S0022053113001439?utm_source=chatgpt.com "Higher order game dynamics - ScienceDirect"
