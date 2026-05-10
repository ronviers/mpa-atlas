# mpa-atlas — next-session handoff

**Status of protocol side:** v0 stable. Full RFC sequence ([RFC-1](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-2](../rfcs/MPA-RFC-2_FDR-Signatures.md), [RFC-3](../rfcs/MPA-RFC-3_Consistency-Completeness.md), [RFC-S](../rfcs/MPA-RFC-S_Scale-Management.md), [RFC-V](../rfcs/MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI](../rfcs/MPA-RFC-RI_Realizer-Interface.md), [RFC-C](../rfcs/MPA-RFC-C-Calibration.md)) ships at thin-pass weight; surface-code and structural-glass reference drivers carry per-substrate calibration sections; schemas at [`schema/`](../schema/) (including `calibration-record.v0.1.json`); architectural commitments captured in [`architecture/MPA_Architectural_Block-In.md`](../architecture/MPA_Architectural_Block-In.md). [v9_compressed.md](../framework/v9_compressed.md) is the operational source of truth on the structural side; [character_compressed.md](../framework/character_compressed.md) on the character side. Repo is public at <https://github.com/ronviers/mpa-atlas>.

**Status of framework side (2026-05-10):** Ten character-projection adoptions cascaded into the operational source of truth — damping/resonance, attractor classification, synchronization, nonequilibrium thermodynamics, information theory, SOC, dissipative structures, control theory, active matter, queueing. All landed as `composition`-type receipts entries (§13–§22). The cascade narrative pushed the original `character_compressed.md` to 64k of connecting tissue; it was renamed to [`character_unabridged.md`](../framework/character_unabridged.md) and a claim-only [`character_compressed.md`](../framework/character_compressed.md) (29k) was rebuilt. [`translating FDR.md`](../framework/translating%20FDR.md) refreshed with §6 cascade summary table. [`H:\mpa-central\RULES.md`](../../mpa-central/RULES.md) refreshed: theory anchors v8 → v9+character; new rule 14 (RFC-S compliance prerequisite) promoted from a tail note. RFC-C v0.2 (2026-05-10) is the operational form of rule 14: it specifies the calibration-record artifact runtime consumes to certify that an RFC-S §4 driver profile is honored at the substrate's current operating point.

**Sibling implementation repo (2026-05-10):** [`H:/mpa-view`](../../mpa-view/) bootstrapped this session — episode loader / calibration pipeline stepper / pattern-library browser per the proposal at [`rfcs/MPA-View_Proposal.md`](../rfcs/MPA-View_Proposal.md). Loads cells from [`H:/mpa-central/library/`](../../mpa-central/library/) and renders MPA-meaningful views (gFDR signature, ground-truth regime overlay). mpa-view's own handoff at `H:/mpa-view/docs/handoff_next_session.md`; this file references it but does not track its open items.

**This file** captures the open items for follow-up sessions in mpa-atlas. Listed roughly in order of pickup priority.

Read in this order before picking up any item:

1. This file.
2. [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md) — foundational principles, three-layer architecture, scope.
3. [v9 compressed](../framework/v9_compressed.md) and [character compressed](../framework/character_compressed.md) — operational source of truth on both projections.
4. [CLAUDE.md](../CLAUDE.md) — repo discipline (thin-RFC + handoff lifecycle).
5. [framework/HANDOFF.md](../framework/HANDOFF.md) — projection discipline (the do-not list lives there).

---

## Open item 1 — Habit-extinction reference driver

**Gating:** mpa-view is now bootstrapped; this item is unblocked. Pick up when behavioral-substrate research is the priority.

Produce [`reference-drivers/habit-extinction.md`](../reference-drivers/) mirroring [`surface-code-qec.md`](../reference-drivers/surface-code-qec.md)'s structure (Header / Operating envelope / Gamut / Translation field / Intents / Reference outputs / Calibration / Limitations / Versioning — note the new Calibration section per RFC-C v0.2). The behavioral-domain second reference; tests the framework's cross-substrate transfer claim — does habit-extinction sit in the same Cugliandolo–Kurchan aging universality class that surface-code QEC instances? If yes, framework's empirical claim validated. If no, that's load-bearing data either way (extension via RFC-Beh or universality-class claim was wrong; both worth knowing).

### Steps

1. **Pick a paradigm** with within-subject acquisition + extinction phases, multiple subjects, ideally spontaneous-recovery and reinstatement (Bouton's context-dependent extinction is one well-characterized line). Publicly available data so `reference_outputs` are reproducible.
2. **Map MPA primitives to substrate** (working hypotheses to test, not commitments):
   - Trail vector $d(t)$ ← EMA of response rate (or response probability) over the kernel window
   - Drive $D = \Phi^*/\kappa$ ← reinforcement rate / dissipation timescale
   - Observer kernel $\tau_{obs}$ ← trial / session / day window
   - Vertex regime $\{c, s, r\}$ ← acquisition plateau / extinction transient / extinguished
   - Edge $\gamma_{AB}$ ← cross-association coupling between Stim-A→Resp and Stim-B→Resp
   - Subgraph $k_{\text{frust}}$ ← behavioral frustration; topology-applies is open question
   - Persistence profile $P$ ← cross-session / cross-context evolution
3. **Characterize gamut** per [RFC-S §4](../rfcs/MPA-RFC-S_Scale-Management.md): $D$-range, $\tau_{obs}$-range $\Pi(S)$, trail-class support, persistence depth $N(S)$. Per [DBS-backward](../architecture/MPA_Architectural_Block-In.md) — be honest about what's NOT covered.
4. **Translation field.** Substrate → canonical (response data → trail vectors → regimes → edges); canonical → substrate (predicted rate from canonical structure).
5. **Per-phase signature targets.** Acquisition trajectory $r \to s \to c$; extinction $s$-aging diagonal with CK slope $\alpha_s$ (the cross-substrate transfer test — same $\alpha_s$ as QEC within tolerance?); spontaneous recovery; reinstatement.
6. **Calibration section.** Per RFC-C v0.2 — per-primitive measurement protocol the calibration record cites: how `L` is read on extinction-curve cessation, how `G₀` is extrapolated from reinforcement-rate sweeps, what counts as the swept `τ_obs` (trial / session / day kernel-width sweep), what perturbation gives a clean `γ_AB`.

### Failure modes (general for behavioral-substrate characterization)

- **Force-fitting** behavioral data into MPA primitives that don't actually fit. Better to honestly report "MPA can't characterize this aspect" — DBS-backward is load-bearing.
- **Over-confident calibration.** Pretending behavioral data is as clean as QEC. Inherit the physical-high / behavioral-medium-low confidence asymmetry.
- **Treating subject heterogeneity as noise.** May be substrate-conditional reading rule, not measurement noise.
- **Pretending to instance universality invariants you can't measure.** If the dataset can't measure $\alpha_s$ at the precision needed, declare the gap.
- **Math envy.** Don't import behavioral-modeling machinery that doesn't earn its weight. Thin discipline applies to drivers too.

### Open questions (don't pretend to close)

- **Static envelope assumption** for subjects whose internal state evolves during measurement (Block-In flags as open frontier).
- **Calibration formalization** for behavioral subjects: subject history? deprivation? time-of-day?
- **Subject heterogeneity:** within-subject vs. between-subject; pick one and declare it.
- **$k_{\text{frust}}$ instancing:** behavioral data may not instance $N_f$ either; both QEC and habit-ext currently lack it. Real cross-substrate gap.
- **Spontaneous-recovery fit:** if it doesn't fit cleanly into $r \to s$ migration, regime taxonomy may need extension.

**Done when:** new file at `reference-drivers/habit-extinction.md` (with Calibration section); README "What's here" updated; Block-In §"Status of sessional artifacts" updated to reflect habit-extinction at v0.1 stable (currently says "Identified, not characterized; queued behind mpa-view bootstrap"); if cross-substrate transfer test succeeds, note in v9 §FDR signatures the second instance of CK aging.

**Effort:** Several hours to days; substrate research, not protocol writing.

---

## Open item 2 — Brain-Langevin reference driver (lower priority)

The library carries 16 brain cells (4 scenarios × 4 ẋ-kinds) under the `mpa-brain` Langevin substrate, but no reference driver exists yet under `reference-drivers/`. Per RULES.md rule 14, framework-canonical observable claims on the brain library require an RFC-S compliant driver. Producing `reference-drivers/brain-langevin.md` is mechanical against the existing library data and the RFC-C v0.2 calibration template — unblocks brain-substrate framework claims that mpa-view will surface.

**Done when:** `reference-drivers/brain-langevin.md` exists with Header / Operating envelope / Gamut / Translation field / Intents / Reference outputs / Calibration / Limitations / Versioning, citing the brain library cells as the round-trip reference dataset.

**Effort:** A few hours; mostly translating the brain library's `tau_env_analytic` table and ẋ-channel definitions into the reference-driver schema.
