# mpa-atlas — next-session handoff

**Status of protocol side:** v0 stable. Full RFC sequence at thin-pass weight: [RFC-1](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-2](../rfcs/MPA-RFC-2_FDR-Signatures.md), [RFC-3](../rfcs/MPA-RFC-3_Consistency-Completeness.md), [RFC-S](../rfcs/MPA-RFC-S_Scale-Management.md), [RFC-V](../rfcs/MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI](../rfcs/MPA-RFC-RI_Realizer-Interface.md), [RFC-C](../rfcs/MPA-RFC-C-Calibration.md). Two reference drivers with Calibration sections: [`surface-code-qec.md`](../reference-drivers/surface-code-qec.md), [`structural-glass.md`](../reference-drivers/structural-glass.md). Schemas at [`schema/`](../schema/) including `calibration-record.v0.1.json`. Architectural commitments in [`architecture/MPA_Architectural_Block-In.md`](../architecture/MPA_Architectural_Block-In.md). [v9_compressed.md](../framework/v9_compressed.md) is the operational source of truth on the structural side; [character_compressed.md](../framework/character_compressed.md) on the character side. Repo public at <https://github.com/ronviers/mpa-atlas>.

**Status of framework side (2026-05-10):** Ten character-projection adoptions cascaded into the operational source of truth — damping/resonance, attractor classification, synchronization, nonequilibrium thermodynamics, information theory, SOC, dissipative structures, control theory, active matter, queueing. All landed as `composition`-type receipts entries (§13–§22). The cascade narrative pushed the original `character_compressed.md` to 64k of connecting tissue; it was renamed to [`character_unabridged.md`](../framework/character_unabridged.md) and a claim-only [`character_compressed.md`](../framework/character_compressed.md) (29k) was rebuilt. [`translating FDR.md`](../framework/translating%20FDR.md) refreshed with §6 cascade summary table. [`H:\mpa-central\RULES.md`](../../mpa-central/RULES.md) refreshed: theory anchors v8 → v9+character; new rule 14 (RFC-S compliance prerequisite) promoted from a tail note. RFC-C v0.2 (2026-05-10) is the operational form of rule 14 — it specifies the calibration-record artifact runtime consumes to certify that an RFC-S §4 driver profile is honored at the substrate's current operating point.

**Sibling implementation repo (2026-05-10):** [`H:/mpa-view`](../../mpa-view/) (<https://github.com/ronviers/mpa-view>) — episode index, substrate-native strip view, X-ratio canonical view (mixes substrate-native data down to the canonical regime-invariant space per RFC-S §1's RG-flow framing). Loads cells from [`H:/mpa-central/library/`](../../mpa-central/library/) and renders them through framework primitives (X-ratio, N_f). mpa-view's own handoff at `H:/mpa-view/docs/handoff_next_session.md`; this file references it but does not track its open items.

**This file** captures the open items for follow-up sessions in mpa-atlas. Listed roughly in order of pickup priority.

Read in this order before picking up any item:

1. This file.
2. [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md) — foundational principles, three-layer architecture, scope.
3. [v9 compressed](../framework/v9_compressed.md) and [character compressed](../framework/character_compressed.md) — operational source of truth on both projections.
4. [CLAUDE.md](../CLAUDE.md) — repo discipline (thin-RFC + handoff lifecycle).
5. [framework/HANDOFF.md](../framework/HANDOFF.md) — projection discipline (the do-not list lives there).

---

## Open item 1 — Per-invariant ẋ-channel declarations in reference drivers

**Earned this session.** mpa-view's X-ratio view surfaced an empirical observation: different ẋ-channels resolve different regime invariants. For structural-glass:

- **Spin-flip** is the right ẋ-channel for reading `N_f` (the k_frust signature). N_f mean = 0.318 at T=1.000 (gt=k) — peak right at T_c, exactly where the framework predicts. X-ratio rarely reaches asymptote in this channel.
- **Spin-relative** is the right ẋ-channel for reading `X-ratio` (and eventually `α_s`). Smooth monotonic locus, X-ratio reaches asymptote across most τ_windows for hot-enough cells.

The reference drivers' Calibration sections currently declare *what* to measure for each MPA primitive, but not *which substrate-native channel* is canonical for each. Add a row to each driver's Calibration table:

| MPA invariant | Canonical ẋ-channel | Why |
|---|---|---|
| `N_f` (k_frust) | spin-flip | resolves transient-negative response on burst-correlated events |
| `X-ratio` (X_c, X_r) | spin-relative | smooth monotonic locus reaches asymptote |
| `α_s` (s-aging slope) | spin-relative | linear segment in χ vs (C₀−C) cleanest in this channel |
| `P_s` (s-plateau) | spin-relative | C(τ)/C(0) plateau visible in continuous overlap signal |

Same kind of declaration for QEC (`detection-event` vs `events-since-snap`) and for any future driver. This is small, concrete, earned evidence.

**Done when:** [`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md) and [`reference-drivers/structural-glass.md`](../reference-drivers/structural-glass.md) Calibration sections gain a "per-invariant ẋ-channel" sub-table; the Calibration record schema either gains a `preferred_xdot_channel` field per invariant or the reference-driver declaration is what it cites.

**Effort:** ~hour, mostly content. Schema change is one optional field.

---

## Open item 2 — Brain-Langevin reference driver

The library carries 16 brain cells (4 scenarios × 4 ẋ-kinds) under the `mpa-brain` Langevin substrate, but no reference driver exists yet under `reference-drivers/`. Per [RULES.md](../../mpa-central/RULES.md) rule 14, framework-canonical observable claims on the brain library require an RFC-S compliant driver. Producing `reference-drivers/brain-langevin.md` is mechanical against the existing library data and the RFC-C v0.2 calibration template — unblocks brain-substrate framework claims that mpa-view will surface.

**Done when:** `reference-drivers/brain-langevin.md` exists with Header / Operating envelope / Gamut / Translation field / Intents / Reference outputs / Calibration / Limitations / Versioning, citing the brain library cells as the round-trip reference dataset, and (per item 1) declaring per-invariant ẋ-channel preferences across `velocity` / `position-relative` / `position-displacement` / `boundary-cross`.

**Effort:** A few hours; mostly translating the brain library's `tau_env_analytic` table and ẋ-channel definitions into the reference-driver schema.

---

## Open item 3 — Habit-extinction reference driver

**Substantive substrate research.** The behavioural-domain second reference; tests the framework's cross-substrate transfer claim — does habit-extinction sit in the same Cugliandolo–Kurchan aging universality class that surface-code QEC instances? If yes, framework's empirical claim validated. If no, that's load-bearing data either way (extension via RFC-Beh or universality-class claim was wrong; both worth knowing).

Produce [`reference-drivers/habit-extinction.md`](../reference-drivers/) mirroring [`surface-code-qec.md`](../reference-drivers/surface-code-qec.md)'s structure (Header / Operating envelope / Gamut / Translation field / Intents / Reference outputs / Calibration / Limitations / Versioning).

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
6. **Calibration section** (per RFC-C v0.2). Per-primitive measurement protocol + per-invariant ẋ-channel declaration (per item 1).

### Failure modes

- **Force-fitting** behavioral data into MPA primitives that don't actually fit. Better to honestly report "MPA can't characterize this aspect" — DBS-backward is load-bearing.
- **Over-confident calibration.** Pretending behavioral data is as clean as QEC. Inherit the physical-high / behavioral-medium-low confidence asymmetry.
- **Treating subject heterogeneity as noise.** May be substrate-conditional reading rule, not measurement noise.
- **Pretending to instance universality invariants you can't measure.** If the dataset can't measure $\alpha_s$ at the precision needed, declare the gap.
- **Math envy.** Don't import behavioral-modeling machinery that doesn't earn its weight. Thin discipline applies to drivers too.

**Done when:** new file at `reference-drivers/habit-extinction.md` (with Calibration section); README "What's here" updated; Block-In §"Status of sessional artifacts" updated to reflect habit-extinction at v0.1 stable; if cross-substrate transfer test succeeds, note in v9 §FDR signatures the second instance of CK aging.

**Effort:** Several hours to days; substrate research, not protocol writing.

---

## Open item 4 — First sealed calibration record (cross-repo, blocking mpa-view's stepper)

**Cross-repo blocker.** RFC-C v0.2 specifies the calibration-record artifact, the schema is at [`schema/calibration-record.v0.1.json`](../schema/calibration-record.v0.1.json), but no record has been produced yet. mpa-view's calibration pipeline stepper (queued in mpa-view's handoff) is blocked on a record existing.

The first record will likely come from running an mpc-glass or mpc-quantum experiment through RFC-C's protocol and emitting a record matching the schema. Likely the structural-glass driver is the easier path — the library cells are already characterized, so the calibration record needs only to certify that one specific cell is in-envelope and supply the measured `{L, G_0, τ_obs_canonical, γ_AB}` with provenance pointers.

**Done when:** at least one sealed calibration record exists somewhere accessible (probably under `H:/mpc-glass/calibration-records/` or `H:/mpa-central/calibration-records/`), conforming to the v0.1 schema, citing the surface-code-qec or structural-glass reference driver as its `driver_profile_ref`.

**Effort:** Probably a session in the relevant `mpc-*` repo; not pure protocol work.

---

## Empirical findings from this session worth reflecting in reference drivers

Surfaced by mpa-view's X-ratio view; should land in `reference-drivers/structural-glass.md` (probably as part of item 1):

1. **N_f peaks at T_c in EA-glass spin-flip.** T=1.000 (gt=k) cell shows N_f mean 0.318 (max 0.500) — empirically highest in the strip. The framework's k_frust signature instances precisely where it should; reference driver's Calibration section can cite this as confirmation.
2. **gt-label vs gFDR-signature disagreement at T=0.200 spin-flip.** gt=c (thermodynamic prior) but N_f ≈ 0.21 (substantial transient-negative response). Either the gt-label needs revision (T<<T_c criterion misses frustration-instantiation in spin-flip channel) or the driver should declare that c-cells in spin-flip show N_f anyway. Calibration discipline ought to specify which wins when label and signature disagree — possibly an addition to RFC-C v0.3.
3. **3-decade clean X-ratio walk in quantum detection-event.** p_base sweep produces monotonic decrease in X across nearly 3 orders of magnitude. The cleanest single-substrate migration in the library; should be the surface-code-qec driver's flagship `reference_outputs` example.
