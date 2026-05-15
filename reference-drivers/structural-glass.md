# Structural-Glass Reference Driver

**Status:** v0.1 — first reference driver for the structural-glass substrate class. Hand-built from [v9 §Fluctuation-dissipation signatures](../framework/v9_compressed.md) (aging-class identification) and [character §gFDR signatures](../framework/cdv1_compressed.md) (Cugliandolo–Kurchan diagonal as the $s$-regime signature).
**Targets:** [RFC-1 v0.2](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-S v0.2](../rfcs/MPA-RFC-S_Scale-Management.md), [RFC-C v0.2](../rfcs/MPA-RFC-C-Calibration.md).
**Schema:** [`schema/driver-profile.v0.2.json`](../schema/driver-profile.v0.2.json) for the profile; [`schema/calibration-record.v0.1.json`](../schema/calibration-record.v0.1.json) for per-experiment calibration. This is the markdown companion; field structure mirrors RFC-S §4.

---

The bootstrap reference for the rheology / amorphous-solid domain. Independent drivers (substrate-implementation drivers in `mpc-glass` and adjacent) are validated against this one via the round-trip protocol of RFC-S §5. Once an independent driver agrees on a shared dataset, the inter-driver-agreement bootstrap takes over and this driver loses sole-authority status. The shared dataset of record is the glass slice of the [mpa-central library](../../mpa-central/library/) — 11 temperatures × 2 ẋ-choices, 1024 realizations per cell, with ground-truth regime labels (`gt: c|s|k|r`) per cell.

## Header

| Field | Value |
|---|---|
| `profile_version` | v0.1 |
| `target_rfc_versions` | RFC-1 v0.2 + RFC-S v0.2 + RFC-C v0.2 |
| `substrate_class` | `structural-glass` |
| `characterization_date` | 2026-05-10 |
| `authority` | reference (hand-built from v9 + character) |
| `validation_history` | empty — first reference |

## Operating envelope

| Field | Content |
|---|---|
| Initial conditions | 3D Edwards–Anderson Ising lattice ($L=16$ default), random ±1 bond disorder, equilibrated above $T_c \approx 0.95$ then quenched. Field $h = 0.1$. |
| Parameter ranges | Temperature $T$ on the library grid: $T \in \{0.20, 0.30, 0.50, 0.70, 0.85, 0.95, 1.00, 1.10, 1.30, 1.50, 1.80\}$; below $T_c$ the substrate ages on the experiment timescale itself. |
| Measurement protocol | Two-time correlation $C(t_w, t_w + \tau)$ and integrated response $\chi(t_w, t_w + \tau)$, ẋ-kind $\in \{\text{spin-flip}, \text{spin-relative}\}$. EMA kernel against spin-overlap signal. |

Calibration verifies (a) thermal-history reproducibility, (b) $h$-field stability, (c) finite-size convergence at the declared $L$ before driver output is trusted.

## Gamut

| Axis | Value |
|---|---|
| $D$-range | $D = \Phi^*/\kappa$, $\Phi^* \sim$ stress-power per CRR, $\kappa \sim$ structural-relaxation rate. Above $T_c$ → $D$ small; deep below $T_c$ → $D$ large but $\tau_{\alpha}$ runs off the experiment window. |
| $\tau_{\text{obs}}$-range $\Pi(S)$ | $T$-dependent; see `tau_env_analytic` per cell in [`MANIFEST.json`](../../mpa-central/library/MANIFEST.json). Below $T_c$ the analytic value is `null` (aging unbounded on experiment timescale); above $T_c$ scales as critical-slowing $z\nu = 6$. |
| Shear-profile envelope | Bond-disorder graph; $\gamma_{AB}$ = cross-correlation of region-localized stress-relaxation trails. |
| Trail-class support | One trail per spin (or per coarse-grained region for spin-relative). Vertex regime: $c$ (deeply frozen, $T \ll T_c$) → $s$ (aging, $T < T_c$) → $k$ (critical, $T \approx T_c$) → $r$ (paramagnet, $T > T_c$). |
| Persistence depth $N(S)$ | Set by ratio of $t_{\text{obs}}$ cap to $\tau_\alpha$; ~1.5 decades past $\tau_{\text{env}}$ at the operating point. |
| Contraction-rate fit | Empirical $\varepsilon_n$ from successive coarse-grainings of two-time correlation; stable below $T_c$, decreases monotonically through the critical slowing. |

## Translation field

**Substrate → canonical:**

1. Raw spin field $\sigma_i(t)$ → ẋ-channel: spin-flip (binary flip events) or spin-relative (continuous overlap signal).
2. Trail vector per region: EMA of ẋ at kernel width $\tau_{\text{obs}}$.
3. Vertex regime: $\lambda_A$ from EMA decay rate; compare to $D$ to read $c$ / $s$ / $k$ / $r$. The library cells' ground-truth `gt` label is the reference reading.
4. Edge $\gamma_{AB}$: cross-correlation of region trails. **Sign convention:** thermal Ising is detailed-balance-respecting at fixed $T$; signs are stable across kernel widths above $T_c$. Below $T_c$ the substrate is non-stationary; treat sign as kernel-width-conditional and prefer $\lvert\gamma\rvert$ + FDR shape jointly.
5. $k_{\text{frust}}$: closed cycles in the bond graph with obstructive shear product. Frustration is structural in EA Ising — every odd plaquette closes; that's the substrate's defining feature.

**Canonical → substrate (round-trip prediction):**

1. Canonical regime → predicted spin-overlap decay rate.
2. Canonical $\gamma$ → predicted region cross-correlation.
3. Canonical persistence-tower → predicted FDR shape vs $\tau_{\text{obs}}$.

**Auto-remap rule.** Generator: differentiated EMA on overlap signal — small kernel-width changes yield linear flow on trail vectors. Finite: integrated EMA at the new kernel width. Multiplicative in MC-sweep counts is the natural unit.

## Intents

| Intent | Supported | Operation | Sacrifice |
|---|---|---|---|
| I1 regime-preserving | yes | scale uniformly to fit substrate $D_{\max}$ at given $T$; preserves $c \to s \to k \to r$ migration with $T$ | absolute $D$, $\gamma$ |
| I2 drive-faithful | yes | exact $D$, $\gamma$ on in-gamut; reject specs above $D_{\max}$ at this $T$ | completeness |
| I3 capacity-preserving | yes | $\lvert \Gamma^* \rvert$ against $\sqrt{2D / \alpha\,\gamma_{\min}\,d_{\text{avg}}}$; pattern-preserving reduction | absolute drive |
| I4 persistence-preserving | yes | $\{\varepsilon_n\}$ across kernel-width ascents; $S_n$ from successive EMA widths | absolute drive, single-position regime |
| I5 signature-preserving | yes | preserves $\{X_c, \alpha_s, P_s, X_r, N_f\}$; $s$-aging Cugliandolo–Kurchan diagonal is the load-bearing signature for $T < T_c$ | exact intra-class parameters |

## Reference outputs (round-trip dataset)

| Input | Expected response | Tolerance |
|---|---|---|
| EA $L=16$, $h=0.1$, $T = 0.50$, ẋ = spin-relative (library cell `glass__T0.500__spin-relative`) | $s$-aging diagonal; Cugliandolo–Kurchan slope $\alpha_s$ in the EA-class universality | I5: universality-class agreement (categorical); intra-class parameter distance < 10% |
| Same code, $T$ swept across $\{0.85, 0.95, 1.00, 1.10\}$ | Locus deforms $s$-aging → $k$-critical → $r$ unit-slope FDR; vertex migrates $s \to k \to r$ | I1: regime-partition Hamming; transition in $T \in [0.95, 1.10]$ |
| Same code, $\tau_{\text{obs}}$ swept across the cell's `tau_windows` grid | $\varepsilon_n$ decreasing across ascents below $T_c$; floors near $T_c$ | I4: $\{\varepsilon_n\}$ sequence distance |

## Calibration

Per-primitive measurement protocol the [RFC-C v0.2](../rfcs/MPA-RFC-C-Calibration.md) calibration record cites for this substrate class. Native libraries: DMA / rheometer SOPs (TA Instruments, Anton Paar) for laboratory rheology; Monte Carlo / molecular-dynamics replica-exchange protocols for the EA-class simulation surface.

| Primitive | Native SOP output | Translation rule | Validation check |
|---|---|---|---|
| **`L`** (structural relaxation rate) | Stress relaxation $\sigma(t) = \sigma_0 \exp[-(t/\tau_\alpha)^\beta]$ on cessation; or simulation analog: spin-overlap autocorrelation after MC quench. | $L = \tau_\alpha^{-1}$ evaluated at the relevant aging time $t_w$. For multi-mode relaxation, take the slowest $\tau_\alpha$ as structural $L$; faster modes are local $\beta$-relaxation. | Cessation complete: no residual drive torque (lab) / no remnant field (simulation). Match to independent creep-compliance viscosity $\eta_0 = 1/(J_e^0 \cdot L)$. |
| **`G₀`** (unsaturated budget) | Steady-state shear stress $\sigma_{\text{ss}}$ at strain rate $\dot\gamma$; or simulation: steady-state energy injection rate per CRR. | $G_0 = \sigma_{\text{ss}} \cdot \dot\gamma / E_{\text{CRR}}$ where $E_{\text{CRR}}$ is the substrate-declared CRR energy scale (or inferred from $G'(\omega)$ plateau). | Extrapolate $\sigma_{\text{ss}} \cdot \dot\gamma$ to zero strain to isolate the unsaturated cost. $G_0 / L > 1$ at max drive. |
| **`τ_obs`** (canonical observer kernel) | Two-time correlation $C(t_w, t_w + \tau)$; or frequency sweep $G'(\omega), G''(\omega)$. | Canonical $\tau_{\text{obs}}$ is the waiting time $t_w$ that maximises gFDR violation in $\chi$ vs $C(0) - C(\tau)$. Alternative: $\omega^*$ where $G' = G''$ (loss-tangent peak), mapped to $\tau_{\text{obs}} = 1/\omega^*$. | gFDR must show the Cugliandolo–Kurchan aging diagonal below $T_c$; if absent, kernel misaligned. |
| **`γ_AB`** (cross-saturation) | Localized shear burst on region $A$; stress response in region $B$. | $\gamma_{AB} = -\partial \sigma_B / \partial \gamma_A$, normalised by local modulus $G'_A$. Sign per v9 Appendix F: negative cooperative (stress shielding), positive conflicting (stress concentration). | Linear-response regime verified by Boltzmann-superposition check. |
| **Threshold (chit) verification** | Strain-rate sweep toward yield; or simulation: drive-rate sweep toward critical $\dot\gamma_c$. | Verify stress-fluctuation linewidth broadens as $\dot\gamma \to \dot\gamma_c$ where $G_0 \to L$. | Threshold crossing coincides with onset of non-Newtonian behaviour and shear banding. |
| **Drift clock** (retirement trigger) | Thermal history drift; physical aging (enthalpy relaxation). | Retire when $\tau_\alpha$ shifts > 20% from baseline, or when sample undergoes thermal excursion outside the calibrated $T$-range. | Structural relaxation time $\tau_\alpha$ is the drift clock; aging changes $L$, which changes the chit. |

The library cells at `H:/mpa-central/library/data/glass/glass__T<...>__<xdot_kind>.json` are the substrate-side reference dataset for round-trip validation under this calibration; `gt: c|s|k|r` per cell is the regime label the canonical reading must reproduce.

## Known limitations

1. **Below-$T_c$ aging is unbounded on the experiment timescale.** The library uses a fallback time grid (`tau_env_analytic = null`) for $T \le T_c$ — the substrate ages on the same clock as the measurement. Calibration records below $T_c$ must declare the aging clock explicitly and accept that the canonical reading is $t_w$-conditional.
2. **`G₀` extrapolation is hard near $T_c$.** Critical slowing pushes the linear-response regime to vanishingly small $\dot\gamma$. Calibration uncertainty on $G_0$ blows up as $T \to T_c$ and the chit becomes diagnostic-flag territory rather than a clean measurement.
3. **Stable operating envelope assumed.** Behavioural / evolving-substrate concerns (RFC-S Appendix C) are absent — a quenched EA lattice does not evolve its bond disorder across the envelope. Aging is in-distribution evolution, not envelope evolution.

## Versioning

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-05-10 | First reference. Substrate-class translation table absorbed from MPA-RFC-C v0.1 §1.2 during the v0.2 thinning. |

**Revisions** require a v0.2+ bump and a row in `validation_history` once an independent driver agrees on a shared dataset (the inter-driver-agreement bootstrap of RFC-S §5).
