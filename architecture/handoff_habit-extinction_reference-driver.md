# Handoff: habit-extinction reference driver

**Status:** Planning document for the second reference driver (behavioral domain). Surface-code QEC is the first, hand-built from v9 §FDR signatures.
**Audience:** A future Claude (or human) coming into this work cold.
**Companion:** [v9 compressed](../framework/v9_compressed.md) (rigor source), [Architectural Block-In](MPA_Architectural_Block-In.md) (especially §"Where this distinction strains" on behavioral substrates), [`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md) (template), [RFC-S §3–§5](../rfcs/MPA-RFC-S_Scale-Management.md), [RFC-2](../rfcs/MPA-RFC-2_FDR-Signatures.md).
**Project memory:** `project_substrate_investment.md` — explains why this is happening now (bootstrap done at v0.1; cross-substrate transfer is the load-bearing test).

---

## Goal

Produce `reference-drivers/habit-extinction.md` at v0.1 — the second reference driver, structurally paralleling surface-code-qec.md but for the behavioral domain. Test the framework's cross-substrate transfer claim: does habit-extinction sit in the same Cugliandolo–Kurchan aging universality class that surface-code QEC instances?

## Why this matters

Surface-code QEC is a clean substrate; the framework's reading rules ported cleanly. Behavior is the harder case the framework was designed for (substrate-neutral working space, observer-driven scale management, demand-bounded sufficiency — all of these were specifically motivated by substrate variability that QEC alone underspecifies). If habit-extinction's signatures match QEC's $\alpha_s$ and $P_s$ within tolerance, the framework's empirical claim is validated. If they don't, that's load-bearing data: either the framework needs extension (RFC-Beh, evolving substrates) or the universality-class claim is wrong, and either is worth knowing.

## What needs to happen

### Step 1: Pick a canonical dataset

Habit-extinction has decades of clean data. Choose one paradigm with:

- Within-subject acquisition + extinction phases (so the trajectory is observable per subject)
- Multiple subjects (for averaging and substrate-class characterization)
- Ideally: spontaneous-recovery and reinstatement phases (Block-In flagged these as load-bearing for the regime taxonomy stress test)
- Publicly available data (so the reference driver's `reference_outputs` are reproducible)

Candidate paradigms (not exhaustive; deeper behavioral expertise may surface better choices):

- **Operant extinction** (lever-press for food → omission of reinforcement). Many published datasets; clean rate-of-response curves.
- **Pavlovian fear extinction** (CS+US conditioning → CS alone). Freezing or galvanic-skin-response data; canonical in fear-learning literature.
- **Drug-seeking extinction** (active lever for drug delivery → saline substitution). Relevant for relapse-prevention applications.

Recommendation: pick one paradigm that has both spontaneous-recovery and reinstatement data published. Bouton's context-dependent extinction work is one well-characterized line.

### Step 2: Map MPA primitives to the substrate

This is the research step. Working hypotheses to test, not commitments:

| MPA primitive | Behavioral candidate |
|---|---|
| Trail vector $d(t)$ | EMA of response rate (or response probability) over the kernel window |
| Drive $D = \Phi^*/\kappa$ | Reinforcement rate / dissipation timescale (decay-without-reinforcement) |
| Observer kernel $\tau_{obs}$ | Window over which rate is read: trial / session / day |
| Vertex regime $\{c, s, r\}$ | Acquisition plateau ($c$) / extinction transient ($s$) / extinguished ($r$) |
| Edge $\gamma_{AB}$ | Cross-association coupling (e.g., between Stim-A→Resp and Stim-B→Resp) |
| Subgraph $k_{\text{frust}}$ | Behavioral frustration: conflicting S-R associations (open question whether topology applies) |
| Persistence profile $P$ | Cross-session / cross-context response evolution |

Spontaneous recovery is interesting: response returns after a delay without re-exposure. Maps to $s$-regime metastability that re-emerges past a transient window? Or to migration $r \to s$ under hidden drive (context cue)? The fit determines whether habit-extinction respects v9 §Compression Axiom's downward extension paragraph.

Reinstatement: response returns after re-exposure. Likely maps cleanly to drive restoration (Stim-Cue raises $D$ → migration $r \to s \to c$).

### Step 3: Characterize the gamut

Per RFC-S §4 driver-profile structure:

- **$D$-range:** What range of reinforcement rates is the dataset characterized for? Below floor, extinction trivial; above ceiling, addictive overtraining regime. Both are out-of-gamut.
- **$\tau_{obs}$-range $\Pi(S)$:** Single-trial reading is noisy; session-level is cleaner; day-level loses trial-by-trial structure. Driver declares the supported range.
- **Trail-class support:** Which canonical structures the substrate hosts. Likely vertex + edge; subgraph $k_{\text{frust}}$ is the open question.
- **Persistence depth $N(S)$:** How many ascents the data supports. Trial → session → day → context = 3-4 levels potentially.

Per **DBS-backward direction** (Block-In §3): be honest about what's NOT covered. If the dataset can't characterize $k_{\text{frust}}$ topology because no conflicting-associations protocol was run, declare that gap rather than pretending coverage.

### Step 4: Translation field

Substrate → canonical: how response data maps to trail vectors (EMA), regimes (threshold on EMA decay), edges (cross-association correlation).

Canonical → substrate: predicted response rate from canonical structure at given $D$ and $\tau_{obs}$.

Auto-remap: how the translation evolves as $\tau_{obs}$ moves trial→session→day. RFC-S Appendix B.1 admits both function and generator forms; the EMA-kernel-widening rule has a clean infinitesimal form for behavioral data too, paralleling the surface-code driver.

### Step 5: Per-phase signature targets

This is where cross-substrate transfer gets tested:

- **Acquisition:** ramp-up to plateau. Predicted FDR shape: trajectory through $r \to s \to c$ as drive accumulates.
- **Extinction:** decline to floor. Predicted FDR shape: $s$-regime aging diagonal with Cugliandolo–Kurchan slope (CK ratio $\alpha_s$). **This is the cross-substrate transfer test.** Same $\alpha_s$ as QEC, within tolerance?
- **Spontaneous recovery:** partial response return after delay. Predicted: residual $s$-regime metastability re-emerges past contraction transient.
- **Reinstatement:** response return after re-exposure. Predicted: drive restoration → migration toward $c$.

### Step 6: Open questions to expect (do not pretend to close)

1. **Static envelope assumption.** Habit-extinction data is collected from subjects whose internal state evolves during the experiment. Block-In §"What about substrates that change during measurement?" flags this as an open frontier. Does the static driver-profile model hold here? If not, declare the gap (DBS-backward) — *don't* force-fit by treating evolving state as noise.
2. **Calibration formalization.** Block-In §5.4 flags behavioral calibration as low-confidence. What counts as "calibrated" for a behavioral subject? Subject history? Deprivation level? Time-of-day? The driver-profile `operating_envelope` field needs concrete content.
3. **Subject heterogeneity.** Within-subject vs. between-subject signatures. Does the framework treat each subject as a separate substrate-instance, or as samples of a population substrate? Both are defensible; pick one and declare it.
4. **$k_{\text{frust}}$ instancing.** Whether behavioral data can instance the negativity index $N_f$ (subgraph frustration) is genuinely open. Surface-code under uncorrelated depolarizing doesn't instance it either — *neither reference driver yet covers this universality invariant*. That's a real gap in cross-substrate evidence; flag it.
5. **Spontaneous-recovery fit.** If it doesn't fit cleanly into $r \to s$ migration, the regime taxonomy may need extension. Better to surface this than paper over it.

## Failure modes to watch

- **Force-fitting.** Behavioral data into MPA primitives that don't actually fit. Better to honestly report "MPA can't characterize this aspect" — DBS-backward direction is load-bearing here.
- **Over-confident calibration.** Pretending behavioral data is as clean as QEC. RFC-S v0.1 §5.4 was explicit that physical-substrate calibration is high-confidence; behavioral is medium-low. Inherit that honesty.
- **Treating subject heterogeneity as noise.** Heterogeneity may be substrate-conditional reading rule, not measurement noise.
- **Pretending to instance universality invariants you can't measure.** If your dataset can't measure $\alpha_s$ at the precision needed for cross-substrate comparison, declare that gap.
- **Math-envy.** Don't import behavioral-modeling machinery that doesn't earn its weight. RFC-S thin-pass discipline applies to drivers too: gross-underengineering at the exchange surface, dense rigor in v9.

## Completion criteria

- New file `reference-drivers/habit-extinction.md` mirroring `surface-code-qec.md`'s structure (Header / Operating envelope / Gamut / Translation field / Intents / Reference outputs / Limitations / Versioning).
- All gaps explicitly declared (DBS-backward); no force-fitting.
- README "What's here" updated with new entry.
- Block-In §"Reference substrates" updated to reflect habit-extinction at v0.1 stable (currently says "Identified, not characterized").
- If the cross-substrate transfer test (matching $\alpha_s$ within tolerance) succeeds: note in v9 §Fluctuation-dissipation signatures the second instance of CK aging.
- If it fails: surface that as data — don't fudge. Either MPA needs extension (RFC-Beh on the roadmap) or the universality-class claim was wrong; both are worth knowing.

## Effort estimate

Substantial — substrate research, not protocol writing. Hours to days, depending on dataset depth and how much subject-side characterization gets covered. The Step 1–2 mapping work is the highest-uncertainty part.

## What this enables

The framework's cross-substrate transfer test is the strongest empirical claim it makes. Until habit-extinction (or another behavioral substrate) is characterized, the framework has one substrate's worth of evidence. After: two substrates with the same universality class would be load-bearing; two substrates with different classes would be load-bearing in a different direction. Either is a real result.
