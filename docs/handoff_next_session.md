# mpa-atlas — next-session handoff

**Status of protocol side:** v0 stable. RFC sequence ([RFC-1](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-2](../rfcs/MPA-RFC-2_FDR-Signatures.md), [RFC-3](../rfcs/MPA-RFC-3_Consistency-Completeness.md), [RFC-S](../rfcs/MPA-RFC-S_Scale-Management.md), [RFC-V](../rfcs/MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI](../rfcs/MPA-RFC-RI_Realizer-Interface.md)) ships at thin-pass weight; surface-code reference driver hand-built from v9 §FDR; schemas at [`schema/`](../schema/); architectural commitments captured in [`architecture/MPA_Architectural_Block-In.md`](../architecture/MPA_Architectural_Block-In.md). [v9_compressed.md](../framework/v9_compressed.md) is the operational source of truth. Repo is public at <https://github.com/ronviers/mpa-atlas>.

**This file** captures the open items for follow-up sessions. None of the items below blocks anything; mpa-atlas can sit indefinitely. Pick one up only when there's a specific reason. Listed roughly in order of value-per-hour.

Read in this order before picking up any item:

1. This file.
2. [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md) — foundational principles, three-layer architecture, scope of this work.
3. [v9 compressed](../framework/v9_compressed.md) — rigor source.
4. [CLAUDE.md](../CLAUDE.md) — repo discipline (thin-RFC + handoff lifecycle).

---

## Open item 1 — v9 architectural-framing back-port

Add a §Foundational principles section near the top of [`framework/v9_compressed.md`](../framework/v9_compressed.md), after §Setting. The five principles (color-management discipline, observer-driven scale management, demand-bounded sufficiency, singular working-space path, thin-RFC discipline) live in the [Block-In §"Foundational principles (consolidated)"](../architecture/MPA_Architectural_Block-In.md) and are inherited by every RFC's §0; v9 itself doesn't currently mention them. Asymmetry: RFCs declare principles that govern the framework v9 carries the rigor for, but v9 doesn't acknowledge them. Hygiene fix: v9 should also declare them, then point at the Block-In for the long-form treatment.

The Block-In §"v9 corrections needed" item 2 flags this as pending; both gates (RFC-1 v0.2, RFC-S v0.2) are stable, so it's unblocked.

**Don't:** re-derive (Block-In carries motivation); add weight beyond ½ page (v9 is dense by design); change existing v9 content (additive insert only); make later v9 sections depend on this section (it's a frame, not a load-bearing dependency); update v9 unabridged (rebuilt from compressed; allowed to lag).

**Done when:** v9_compressed has the section after §Setting; Block-In §"v9 corrections needed" item 2 moves from *Pending* to *Closed* with a one-line note pointing at it.

**Effort:** ~15 minutes.

---

## Open item 2 — Habit-extinction reference driver

Produce [`reference-drivers/habit-extinction.md`](../reference-drivers/) mirroring [`surface-code-qec.md`](../reference-drivers/surface-code-qec.md)'s structure (Header / Operating envelope / Gamut / Translation field / Intents / Reference outputs / Limitations / Versioning). The behavioral-domain second reference; tests the framework's cross-substrate transfer claim — does habit-extinction sit in the same Cugliandolo–Kurchan aging universality class that surface-code QEC instances? If yes, framework's empirical claim validated. If no, that's load-bearing data either way (extension via RFC-Beh or universality-class claim was wrong; both worth knowing).

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

**Done when:** new file at `reference-drivers/habit-extinction.md`; README "What's here" updated; Block-In §"Reference substrates" updated to reflect habit-extinction at v0.1 stable (currently says "Identified, not characterized"); if cross-substrate transfer test succeeds, note in v9 §FDR signatures the second instance of CK aging.

**Effort:** Several hours to days; substrate research, not protocol writing.
