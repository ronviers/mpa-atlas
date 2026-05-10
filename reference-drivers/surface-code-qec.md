# Surface-Code Reference Driver

**Status:** v0.1 — first reference driver. Hand-built from [v9 §Fluctuation-dissipation signatures](../framework/v9_compressed.md) (surface-code identification) and [v9 §Substrate-conditional reading rules](../framework/v9_compressed.md) (F.1 Markovian sign, F.2 detection events).
**Targets:** [RFC-1 v0.2](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-S v0.2](../rfcs/MPA-RFC-S_Scale-Management.md).
**Schema:** [`schema/driver-profile.v0.2.json`](../schema/driver-profile.v0.2.json). This is the markdown companion; field structure mirrors RFC-S §4.

---

The bootstrap reference for the physical-substrate domain. Subsequent drivers (substrate-implementation drivers in `mpc-*` repos) are validated against this one via the round-trip protocol of RFC-S §5. Once an independent driver agrees on a shared dataset, the inter-driver-agreement bootstrap takes over and this driver loses sole-authority status.

## Header

| Field | Value |
|---|---|
| `profile_version` | v0.1 |
| `target_rfc_versions` | RFC-1 v0.2 + RFC-S v0.2 |
| `substrate_class` | `surface-code-qec` |
| `characterization_date` | 2026-05-08 |
| `authority` | reference (hand-built from v9) |
| `validation_history` | empty — first reference |

## Operating envelope

| Field | Content |
|---|---|
| Initial conditions | Surface-code patch initialized to logical-Z eigenstate. Distance-3 rotated geometry. |
| Parameter ranges | Physical error rate $p \in [0, p_{th}]$, $p_{th} \approx 0.01$ (sub-threshold). At and above threshold the locus deforms; reading rules below assume sub-threshold. |
| Measurement protocol | Memory-Z syndrome extraction at fixed cycle interval. Sampling = inverse stabilizer-extraction cycle. Kernel = EMA against detection events (F.2). |

Calibration verifies (a) initial state, (b) physical-error-rate sampling, (c) extraction-cadence stability before driver output is trusted.

## Gamut

| Axis | Value |
|---|---|
| $D$-range | $D = \Phi^*/\kappa$, $\Phi^* \sim$ syndrome-extraction work, $\kappa \sim$ depolarizing rate. Sub-threshold → $D \gg 1$. |
| $\tau_{obs}$-range $\Pi(S)$ | [single-cycle, many-cycle aggregate]. Floors below cycle interval; ceiling at decoherence time. |
| Shear-profile envelope | Stabilizer-graph topology (rotated geometry). $\gamma_{AB}$ = cross-correlation of detection-event trails. |
| Trail-class support | One trail per stabilizer. Vertex regime: $c$ at sub-threshold → $s$ near threshold → $r$ above. |
| Persistence depth $N(S)$ | $\sim$ decoherence-time / cycle-time. ~10–100 cycles practically; signal floors past that. |
| Contraction-rate fit | Empirical $\epsilon_n$ from successive coarse-grainings of detection-event streams; sub-threshold gives $\epsilon < 1$. |

## Translation field

**Substrate → canonical:**

1. Raw stabilizers $s_i(t)$ → detection events $e_i(t) = s_i(t) \oplus s_i(t-1)$ (F.2 canonical preprocessing; bounded-local — an error at $t$ triggers exactly two events).
2. Trail vector per stabilizer: EMA of $e_i$ at kernel width $\tau_{obs}$.
3. Vertex regime: $\lambda_A$ from EMA decay rate; compare to $D$ to read $c$ / $s$ / $r$.
4. Edge $\gamma_{AB}$: cross-correlation of trails. **Sign caveat (F.1):** Markovian substrate; $\gamma$-signs may invert as kernel-width artifact — use $\lvert\gamma\rvert$ + FDR shape jointly, not signs.
5. $k_{\text{frust}}$: closed cycles in stabilizer graph with obstructive shear product. Empty under uncorrelated depolarizing (frustration-free); correlated-noise conditions can close loops.

**Canonical → substrate (round-trip prediction):**

1. Canonical regime → predicted stabilizer-flip rate.
2. Canonical $\gamma$ → predicted cross-correlation.
3. Canonical persistence-tower → predicted FDR shape vs $\tau_{obs}$.

**Auto-remap rule (admits both forms per RFC-S Appendix B.1).** Generator: differentiated EMA — infinitesimal kernel-width change yields linear flow on trail vectors. Finite: integrated EMA at the new kernel width. Multiplicative in cycle counts is the natural unit.

## Intents

| Intent | Supported | Operation | Sacrifice |
|---|---|---|---|
| I1 regime-preserving | yes | scale uniformly to fit substrate $D_{\max}$ at given $p$; preserves $c \to s \to r$ migration | absolute $D$, $\gamma$ |
| I2 drive-faithful | yes | exact $D$, $\gamma$ on in-gamut; reject specs above $D_{\max}$ | completeness |
| I3 capacity-preserving | yes | $\lvert\Gamma^*\rvert$ against $\sqrt{2D/\alpha\gamma_{\min}d_{\text{avg}}}$; pattern-preserving reduction | absolute drive |
| I4 persistence-preserving | yes | $\{\varepsilon_n\}$ across kernel-width ascents; $S_n$ from successive EMA widths | absolute drive, single-position regime |
| I5 signature-preserving | yes | preserves $\{X_c, \alpha_s, P_s, X_r, N_f\}$ — sub-threshold signature is Cugliandolo–Kurchan $s$-aging | exact intra-class parameters |

## Reference outputs (round-trip dataset)

| Input | Expected response | Tolerance |
|---|---|---|
| Distance-3 rotated memory-Z, $p = 0.001$ | $s$-aging diagonal; $\alpha_s$, $P_s$ in Cugliandolo–Kurchan class | I5: universality-class agreement (categorical); intra-class parameter distance < 10% |
| Same code, $p$ swept toward $p_{th}$ | Locus deforms $s$-aging → $r$ unit-slope FDT; vertex migrates $c \to s \to r$ | I1: regime-partition Hamming; transition near $p_{th}$ |
| Same code, $\tau_{obs}$ swept across [1, 10] cycles | $\varepsilon_n$ decreasing across ascents; signal floors at $N(S)$ | I4: $\{\varepsilon_n\}$ sequence distance |

## Calibration

Per-primitive measurement protocol the [RFC-C v0.2](../rfcs/MPA-RFC-C-Calibration.md) calibration record cites for this substrate class. Native libraries: Qiskit Experiments (RB, interleaved RB, GST, T₁/T₂); Stim (syndrome extraction benchmarking); CaliQEC (drift tracking); vendor hardware parameter tables (IBM, Google).

| Primitive | Native SOP output | Translation rule | Validation check |
|---|---|---|---|
| **`L`** (logical decay rate) | Logical fidelity decay during a syndrome-extraction *pause* (cessation). | Fit $F_L(t) = \exp(-Lt)$ during the pause. For multi-exponential decay, the slowest component is the logical $L$; faster components are sub-logical leakage. | Residuals stationary (no hidden EC). Match to independent RB-derived error budget. |
| **`G₀`** (unsaturated budget) | Syndrome extraction rate $f$ × decoder success probability $p_{\text{dec}}$. | $G_0 = f \cdot p_{\text{dec}} / E_{\text{logical}}$ where $E_{\text{logical}}$ is the substrate-declared energy scale of one logical-qubit cycle. Extrapolate to zero logical population if $p_{\text{dec}}$ shows saturation. | $G_0 / L > 1$ at max drive; otherwise out of gamut. |
| **`τ_obs`** (canonical observer kernel) | Syndrome-round window $N \cdot T_{\text{cycle}}$. | Sweep $N$. Canonical $\tau_{\text{obs}}$ is the window that maximises gFDR violation $\int \lvert X(\tau) - 1\rvert\, d\tau$ and reveals the $c \to s \to r$ migration. Valid range $[N_{\min}, N_{\max}]$ declared. | gFDR plot must show distinct regime loci; if only $r$-like, reject (too noisy or too close to Boolean). |
| **`γ_AB`** (cross-saturation) | Targeted logical-operator error on qubit $A$; syndrome-density change on qubit $B$. | $\gamma_{AB} = \partial(\text{syndrome}_B)/\partial(\text{error}_A) \cdot (G_{0,B} / G_{0,A})$, normalised by local budget. Sign per v9 Appendix F.1: negative cooperative, positive conflicting. | Linear in perturbation for $\varepsilon / G_0 < 0.1$. Nonlinear → expand to field kernel (RFC-C Appendix B.1). |
| **Threshold (chit) verification** | Noise-scale sweep $s$ rescaling $T_1, T_2$; logical error per cycle. | Verify the $p_L$ threshold aligns with $\ln(G_0/L) \to 0$ within $\delta G_0/G_0$. | Threshold crossing must coincide with Schawlow–Townes-style linewidth broadening in syndrome variance. |
| **Drift clock** (retirement trigger) | CaliQEC drift model $p(g, t) = p_0 \cdot 10^{t/T_{\text{drift}}}$. | Retire when the drift model predicts $G_0/L$ crossing below 1, or when $T_{\text{drift}} < 5\times$ expected experiment duration. | Drift exceeds 20% of calibrated $\gamma_{AB}$ → retire. |

The library cell at `H:/mpa-central/library/data/quantum/quantum__p<...>__detection-event.json` is the substrate-side reference dataset for round-trip validation under this calibration; `gt: c|s|k|r` per cell is the regime label the canonical reading must reproduce.

## Known limitations

1. **No frustration $N_f$ under uncorrelated depolarizing.** Random errors drive vertex migration $s \to r$ rather than closing frustrated stabilizer-graph loops. Correlated-noise test conditions are needed to instance $N_f$ universality on this substrate.
2. **Auto-remap admits both function and generator forms here** (EMA has a clean infinitesimal rule). Less Markovian substrates may not — this driver does not generalize the Both-Forms-Admissible decision.
3. **Stable operating envelope.** Behavioral / evolving-substrate concerns (RFC-S Appendix C) are absent — surface-code patches do not evolve across the envelope.

## Versioning

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-05-08 | First reference. Hand-derived from v9 §Fluctuation-dissipation signatures and §Substrate-conditional reading rules. |

**Revisions** require a v0.2+ bump and a row in `validation_history` once an independent driver agrees on a shared dataset (the inter-driver-agreement bootstrap of RFC-S §5).
