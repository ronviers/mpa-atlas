# cFDT First Analysis: Smoke-Data Test on Glass and QEC Substrates

**Status:** First operationalization of cFDT predictions on existing data. Smoke-scale results from mpc-glass and mpc-quantum sweep_g runs (2026-05-05).
**Spec:** [`mpa character framework.md`](mpa%20character%20framework.md).
**Apparatus:** [`mpa character holding apparatus.md`](mpa%20character%20holding%20apparatus.md), §3.
**Translation:** [`translating FDT.md`](translating%20FDT.md). The cFDT predictions tested here come from §"Per-regime cFDT predictions" of that document.
**Data sources:**
- `H:/mpc-glass/docs/results/sweep_g_glass_20260505_081934.json` — 3D EA Ising, L=16, t_w=200, t_obs=10000, four scenarios (frozen T=0.3, aging T=0.66, critical T=1.0, paramagnetic T=1.5) × two xdot_kinds (spin-flip, spin-relative).
- `H:/mpc-quantum/docs/results/sweep_g_quantum_20260505_080435.json` — distance-3 surface code, four scenarios (deep-r p=0.0001, deep-s p=0.001, smoke p=0.005, near-thr p=0.02) × two xdot_kinds (detection-event, events-since-snap).

---

## Summary

cFDT predicts that imposed/emergent/critical coherence regimes produce distinct fluctuation-dissipation signatures: imposed is window-invariant with shallow aging diagonal; emergent has pronounced multi-window migration; critical is scale-invariant with power-law statistics. The mpc-glass and mpc-quantum sweep_g data already collect $C_d, C_d^{\text{diag}}, \chi_d, f$ across multiple $\tau_{obs}$ values, which is the raw material cFDT predictions speak to.

**First-pass finding:** the *direction* of multi-window migration in this smoke data does not cleanly separate the cFDT regime predictions. The verbal claim that "emergent has the most migration; critical has the least" is not borne out. What the data does show is real and structured cross-scenario variation in migration patterns, just not the pattern cFDT's verbal predictions specified.

This is operationalization producing a real result: cFDT's regime-signature predictions need refinement, and the smoke-scale data may not be in a parameter regime where the predictions can be cleanly tested. The framework's central claim (regimes have *distinct* signatures) is not contradicted; the *specific* claim about migration as the discriminator is.

---

## What was tested

For each scenario, computed two migration metrics across the eleven $\tau_{obs}$ values at the late-time sample ($\Delta t = 10000$):

- **X-migration:** range of $X = \chi_d / (C_d^{\text{diag}} - C_d)$ (the FDT-violation factor up to a $T$ factor that's the same across windows). Larger range = more multi-window dependence.
- **f-migration:** range of $f = (C_d^{\text{diag}} - C_d)/C_d^{\text{diag}}$ (the v8 fractional-decorrelation reading). Bounded [0,1]; doesn't blow up.

cFDT predicts:
- Imposed coherence: small migration on both metrics
- Emergent coherence: large migration
- Critical coherence: small migration but with non-Lorentzian (power-law) statistical signature

---

## Glass results (spin-relative xdot, the meaningful reading)

| Scenario | $T$ | gt | X-mig | f-mig | cFDT-predicted regime | cFDT-predicted migration |
|---|---|---|---|---|---|---|
| frozen | 0.30 | c | 1.451 | 0.11 | imposed (held by quenched disorder + low T) | LOW |
| aging | 0.66 | s | 0.330 | 0.05 | emergent (canonical glass aging) | HIGH |
| critical | 1.00 | k | 0.293 | 0.09 | critical (near $T_g$) | LOW (with power-law signature) |
| paramagnetic | 1.50 | r | 0.234 | 0.22 | degenerate (no holding) | — |

**Predicted ordering (by migration):** aging > frozen ≈ critical ≈ paramagnetic.
**Observed ordering (X-mig):** frozen >> aging > critical > paramagnetic.
**Observed ordering (f-mig):** paramagnetic > frozen > critical > aging.

Aging shows the *lowest* f-migration of the four scenarios. The cFDT prediction that emergent shows pronounced migration is contradicted at this scale. Frozen shows huge X-migration but small f-migration — the X-range is dominated by an outlier at the largest $\tau_{obs}$ where the small denominator ($C_d^{\text{diag}} - C_d \approx 0$) produces an inflated $X$ value.

Spin-flip xdot results are degenerate (f-values all ≈1.00 across windows) — the trail-disorder structure is not informative under that xdot kind for these parameters.

## Quantum results

| Scenario | $p_{base}$ | gt | X-mig (det-ev) | f-mig (det-ev) | f-mig (events-since-snap) | cFDT-predicted regime |
|---|---|---|---|---|---|---|
| deep-r | 0.0001 | r | 8814 | 0.16 | 0.64 | degenerate (no holding) |
| deep-s | 0.001 | s | 2013 | 0.54 | 0.90 | s-regime (could be imposed or emergent) |
| smoke | 0.005 | s | 277 | 0.63 | 0.73 | s-regime |
| near-thr | 0.02 | k | 87 | 0.76 | 0.41 | critical (near threshold) |

**Predicted ordering (by migration):** deep-s/smoke > near-thr (critical predicted to NOT migrate).
**Observed (X-mig):** monotonically decreasing with $p$ — deep-r highest, near-thr lowest.
**Observed (f-mig, detection-event):** monotonically increasing with $p$ — near-thr highest.

Detection-event and events-since-snap give different f-migration orderings, consistent with the substrate-conditional reading rule (F-002/F-003 in mpc-quantum's footing). Neither matches the cFDT verbal prediction directly:

- **X-mig** is dominated by small denominators at low error rate; not directly comparable to glass.
- **f-mig (detection-event)** shows near-threshold with the *largest* migration, opposite to cFDT's "critical = scale-invariant" prediction.
- **f-mig (events-since-snap)** is non-monotonic and shows near-threshold with the *smallest* migration — consistent with cFDT's critical-as-scale-invariant prediction *for this xdot kind only*.

## What this means

**The cFDT verbal predictions don't cleanly hold in this data.** Three possible reasons, ranked by my read:

1. **Smoke-scale parameter regime.** The data is from smoke runs (L=16, n_realizations=16-32, t_obs=10000, t_w=200). Production-scale runs (L=24+, more realizations, longer t_obs, longer t_w) may give cleaner signals. mpc-glass's roadmap explicitly schedules production runs for Phase 3.
2. **Mapping from physical scenarios to cFDT regimes is uncertain.** I assumed glass-aging maps to emergent and glass-critical to critical. Both could plausibly map elsewhere. For glass at $T=0.66$ with field $h=0.1$, the holding has both quenched-disorder structure (emergent-like) and field-driven character (imposed-like). cFDT's regime trichotomy may not map onto the physical scenarios as I sketched in the translation document.
3. **Migration as a single metric is too coarse.** cFDT's predictions are about parametric-plot *shape* (Lorentzian vs power-law, smooth vs fractal) and statistical character (Gaussian vs heavy-tailed), not just migration range. A richer metric — slope of the parametric plot, autocorrelation decay shape, spectral density — might separate the regimes where the migration metric doesn't.

**What the data does show:** real and structured cross-scenario variation. The xdot kind matters substantially. The substrate-conditional reading principle (F-002/F-003) is operative. The cFDT framework's *general* claim — that regimes have distinct signatures — survives. The *specific* claim about migration as the discriminator is the part that needs refinement.

**The cFDT framework is not falsified by this analysis.** It also isn't validated. The data is in a parameter regime that doesn't cleanly separate the predictions, and the verbal predictions themselves are coarser than the framework allows.

## Recommendations

1. **Refine the cFDT predictions** in [`translating FDT.md`](translating%20FDT.md). The migration-as-discriminator framing is too verbal. Replace with: parametric-plot shape characterization (Lorentzian fit residual, power-law exponent, fractal dimension of the curve), autocorrelation decay shape (single-exponential vs stretched-exponential vs power-law), and spectral character (Lorentzian vs $1/f^\alpha$ vs colored). Each regime predicts a specific combination of these — quantitative, not just verbal.
2. **Wait for production-scale data** before claiming cFDT predictions hold or fail. mpc-glass Phase 3 production-scale runs (L=24+ at $T=0.66$, longer timescales, more realizations) will give better-separated signal. mpc-quantum at higher distance and longer t_obs likewise.
3. **Reconsider the scenario→cFDT-regime mapping.** Glass-aging may not be emergent; it may be imposed (driven by $h$) or mixed. Critical-coherence in glass may require parameters beyond just $T = T_g$ — possibly a system specifically tuned to operate AT threshold rather than near it. The mapping should be derived from the substrate's actual operating-mode characterization, not assumed from temperature alone.
4. **Do not yet write `cFDR demonstration glass.md` and `cFDR demonstration qec.md`.** Those documents would have asserted cFDT regime-classifications for those substrates; based on this analysis, the classifications aren't ready. Write the demonstrations after the verbal predictions are refined and production data is in.

## Reproducibility

The analysis above is reproducible from the JSON data with this Python:

```python
import json, numpy as np

def analyze(path):
    with open(path) as f: data = json.load(f)
    for r in data['results']:
        last = r['last_sample']
        x_ratios, f_values = [], []
        for pw in last['per_window']:
            denom = pw['C_d_diag'] - pw['C_d']
            if abs(denom) > 1e-9:
                x_ratios.append(pw['chi_d'] / denom)
            f_values.append(pw['f'])
        x_arr = np.array(x_ratios); f_arr = np.array(f_values)
        print(f"{r['scenario']:>14s} ({r['xdot_kind']:>20s}): "
              f"X-mig={x_arr.max() - x_arr.min():>8.3f}  "
              f"f-mig={f_arr.max() - f_arr.min():.3f}")

for p in ['H:/mpc-glass/docs/results/sweep_g_glass_20260505_081934.json',
          'H:/mpc-quantum/docs/results/sweep_g_quantum_20260505_080435.json']:
    print(p); analyze(p); print()
```

## What this exercise is and is not

It is a first contact between cFDT predictions and real data — the operationalization the framework's directive in §10 of the spec called for. It produced a real result: the verbal predictions need refinement, the smoke-scale data doesn't separate the regimes cleanly, the framework's general claim survives but needs sharpening before being tested again.

It is not a falsification of cFDT. It is not a validation. It is a finding that operationalization at this scale changes what counts as a useful next step: refine the predictions to be quantitative, then test on production-scale data, then return to the demonstration documents on glass and QEC vocabularies.

---

## Library-data follow-up (H:/mpa-central, 2026-05-05)

The smoke analysis above used `sweep_g` runs (2026-05-05) — exploratory, fixed time grids, n_real=16-32. The mpa-central library (`H:/mpa-central/library/`) contains higher-quality data for the same observables: 11-point glass T-sweep through Tc, 4-point quantum p-sweep across threshold, τ_env-anchored time grids per operating point, n_real=1024 for glass and 16384 (16×1024) for quantum, mean+SEM throughout, 31 τ_obs per operating point. Cross-substrate analyses are pre-registered at `H:/mpa-central/pre_registered/`. The library is the right surface for cFDT analysis going forward; the smoke analysis above is historical first-pass.

### What the library data shows

For each operating point under the snapshot-relative ẋ choice (rule 12's discriminating coordinate), at the late-time samples (last 8 of 28 dt-points, in the broad-τ × late-dt corner), I computed three shape characterizations of the parametric plot:

- **R² of linear fit** of $\chi_d$ vs $(C_d^{\text{diag}} - C_d)$. High R² ⇒ smooth FDR locus; low R² ⇒ non-smooth (cFDT critical-regime would predict low R²).
- **FDR slope** (linear-fit slope $b$). Standard-FDR derived $X$ proxy.
- **Decay exponent α** of $(C_d^{\text{diag}} - C_d) \sim dt^\alpha$ at late dt (log-log fit). Power-law decay ⇒ aging / NESS / critical.

**Glass (spin-relative, 11 T values, at τ~100, late dt):**

| T | gt | R² | slope | <X> | α |
|---|---|---|---|---|---|
| 0.200 | c | 0.637 | +0.0010 | +0.236 | +0.294 |
| 0.300 | c | 0.997 | +0.0066 | +0.111 | +0.562 |
| 0.500 | s | 0.980 | +0.0036 | +0.020 | +0.520 |
| 0.700 | s | 0.977 | +0.0030 | +0.016 | +0.442 |
| 0.850 | s | 0.989 | +0.0033 | +0.015 | +0.410 |
| 0.950 | k | 0.968 | +0.0031 | +0.015 | +0.386 |
| 1.000 | k | 0.987 | +0.0031 | +0.015 | +0.371 |
| 1.100 | r | 0.942 | +0.0029 | +0.015 | +0.350 |
| 1.300 | r | 0.919 | +0.0013 | +0.008 | +0.261 |
| 1.500 | r | 0.992 | +0.0039 | +0.018 | +0.396 |

**Quantum (events-since-snap, 4 p values, at τ~100, late dt):**

| p_base | gt | R² | <X> | α |
|---|---|---|---|---|
| 1e-4 | r | 0.004 | +13232 | +0.015 |
| 1e-3 | s | 0.435 | +1105 | +0.021 |
| 2e-3 | s | 0.604 | +595 | -0.003 |
| 1e-2 | s | 0.790 | +95 | +0.030 |

### Findings vs cFDT predictions

**Prediction 1 — "Critical coherence has scale-invariant (fractal-like) parametric plot, low R² in linear fit."** *Not supported.* Glass at T=0.95 and T=1.0 (gt=k, near Tc, the most-likely-critical operating points) show R² = 0.968 and 0.987 — among the *smoothest* parametric plots in the entire sweep. The frozen scenario at T=0.2 has the *lowest* R² at small τ, which is opposite to the imposed-regime prediction.

**Prediction 2 — "Critical coherence has 1/f spectrum / power-law statistics with distinct exponent at Tc."** *Not supported.* Decay exponent α is roughly 0.3–0.6 across ALL glass T values, with no special signature at Tc. The whole T sweep behaves like a NESS with power-law-like decay; no operating point separates as "critical" by α alone.

**Prediction 3 — "Imposed coherence stays close to FDT (X≈1) at short times."** *Mostly not supported.* Slope and X values vary continuously across T with no sharp transition. The closest-to-FDT cases (slope ~0.003, X ~0.015) include both gt=s and gt=k operating points — the imposed-vs-emergent boundary doesn't show up in this slope.

**Prediction 4 — "Each regime has distinct signature."** *Supported in spirit, not in specifics.* Operating points DO produce distinct (R², slope, X, α) signatures, but the distinction doesn't fall along the imposed/emergent/critical axis I claimed. Glass scenarios cluster differently — by raw temperature, not by predicted regime.

**Prediction 5 — "Quantum X-walk has hump shape with peak ξ ∈ [0.3, 0.6]."** *Supported (already established in Test 1 addendum).* The library data confirms the X-hump pattern: low p (deep-r) shows degenerate parametric plot (R²=0.004); higher p shows progressively cleaner FDR with R² rising. This is a substrate-specific scaling that the existing pre-registered analysis already documented.

### Critical caveat: this test was not RFC-S-compliant

The analysis above interpreted parametric-plot characterizations at $\tau_{obs} \in \{10, 100, 1000\}$ as tests of cFDT regime predictions. That interpretation overreaches.

[`MPA-RFC-S_Scale-Management.md`](../rfcs/MPA-RFC-S_Scale-Management.md) §1–§2 says the canonical representation of any operating point is parametrized by $(\tau_{obs}, D)$, with the substrate's gamut declaring its $(D, \tau_{obs})$ envelope, and observer positions chosen via the auto-remap rule under a declared intent. v9 §Three-typed-objects classifies regime by where $\lambda_A$ sits relative to $D$. To produce a framework-correct regime reading at any operating point, the substrate must emit $D$ (or $(\Phi^*, \kappa)$); $\tau_{obs}$ must be set inside the substrate's $\Pi(S)$ via RFC-S protocol; and the prediction under test must be stated in $(D, \tau_{obs})$-space rather than absolute observable space.

None of those three are in place for this analysis:

- **$D$ is not emitted.** The library files contain $T$, $p_{base}$, $h_{field}$ and the scenario gt-label, but no $D$ value. The c/s/k/r ground-truth labels are assigned from substrate physical knowledge (low T = c, near $T_c$ = k, etc.), not from a $\lambda_A / D$ reading. Without $D$, regime classification is substrate-conventional, not framework-canonical.
- **$\tau_{obs}$ scheduling is τ_env-anchored, not RFC-S-compliant.** The library's per-operating-point time grids (per [`H:/mpa-central/library/LIBRARY_SPEC.md`](file:///H:/mpa-central/library/LIBRARY_SPEC.md)) are a useful step but they are not driver-profile-declared, do not name an intent, and do not implement the auto-remap rule across $\tau_{obs}$ that RFC-S §1 specifies. Glass at $T \ll T_c$ has unbounded $\tau_{env}$ and the library uses a fallback grid; that operating point is read at $\tau_{obs}$ values whose relation to the substrate's actual scale-relativity structure is undefined.
- **cFDT regime predictions are not stated in $(D, \tau_{obs})$-space.** The translation document specifies regime signatures verbally (parametric-plot shape, multi-window migration, decay exponent) without anchoring them to observer position relative to substrate drive. An operating point predicted to be "critical" is a claim about its location in $(D, \tau_{obs})$-space; the prediction can only be tested against measurements at that location.

**Verdict shift.** The analysis above does not show "library data shows cFDT predictions don't hold." It shows "the parametric-plot characterizations at ad hoc $\tau_{obs}$ on operating points without $D$ produce these numbers, which do not separate by gt-label as I had hoped." That is a measurement, not a framework test. cFDT regime predictions remain untested.

### Net assessment

cFDT's general claim — that coherence regimes have distinct fluctuation-dissipation signatures — is neither supported nor falsified by this work. The specific predictions in the translation document remain conjectures awaiting an RFC-S-compliant test. The numerical findings (R², slopes, α exponents per operating point) are valid measurements that may turn out to align or fail to align with cFDT predictions once the predictions are stated in $(D, \tau_{obs})$-space and the substrates emit $D$.

What the data shows is *richer* than what cFDT's verbal predictions specify:

- The parametric plots are remarkably smooth (high R²) across most operating points, and across both substrates. This is *not* what cFDT predicted for critical operation.
- The decay exponent α is power-law-like across the full glass T-sweep, with no special signature at Tc. The "1/f spectrum at criticality" prediction doesn't appear.
- The substrate-conditional reading (rule 7) is doing more work than the cFDT regime classification. Glass and quantum show fundamentally different signatures even when their gt-labels match (s on glass T=0.5–0.85 vs s on quantum p=1e-3 to 1e-2).

### Prerequisites for a proper cFDT test

A real cFDT operationalization requires three pieces of infrastructure that are not in place:

1. **$D$ emission per operating point.** The substrate's RFC-S `operating_envelope` must declare $(\Phi^*_{\min/\max}, \kappa_{\min/\max})$ at each operating point so $D = \Phi^*/\kappa$ is computable. Currently substrates emit $T$ or $p_{base}$ (the substrate-native control parameter) but not $D$. Substrate-side primitive update owed.
2. **RFC-S-compliant $\tau_{obs}$ scheduling.** Driver profiles per substrate, declaring $\Pi(S)$ (observer-range) and the auto-remap rule. The library's $\tau_{env}$-anchored sampling is one input but is not a driver profile. RFC-S compliance owed.
3. **cFDT regime predictions re-stated in $(D, \tau_{obs})$-space.** [`translating FDT.md`](translating%20FDT.md) §"Per-regime cFDT predictions" needs to specify: imposed/emergent/critical as positions or trajectories in $(D, \tau_{obs})$-space, not as absolute observable shapes. What observer position at what $D$ produces which signature, under which intent.

Once these three are in place, cFDT regime predictions become testable on the same library infrastructure (with $D$ added to the per-cell metadata). The numerical analysis machinery used here transfers; only the interpretation needs to be redone.

**Subordinate recommendations** (operational consequences of the prerequisites):

- The $\tau_{env}$-emission already owed in `H:/mpa-central/library/TAU_ENV_OWED.md` is a step toward RFC-S compliance but is not sufficient on its own; $\Phi^*$ and $\kappa$ also need substrate-side emission.
- Higher-order observables (raw-readout autocorrelation timescales, fluctuation-moment skew/kurt, memory-kernel structure) may also be needed depending on how cFDT predictions get re-stated, but should be specified by the predictions, not adopted speculatively.
- The cFDR demonstrations on glass and QEC vocabularies (option 2 from the earlier discussion) remain not-ready until the prerequisites are addressed and cFDT's regime predictions are properly re-stated.

### What this exercise produced

It produced a pair of findings the framework needed:

1. **A clear specification of what cFDT testability requires.** Three prerequisites named, each tractable. The framework knows what it's owed and from where (substrate-side primitive updates, driver profiles, translation-document revision).
2. **A refined understanding of the smoke-vs-library data quality jump.** The library is dramatically better than smoke; it still isn't enough by itself for RFC-S-compliant tests. The library + $D$ + driver profiles + revised cFDT predictions is what's needed.

The earlier verdict ("verbal predictions don't hold under library-grade data") overreached. The corrected verdict is: the test wasn't RFC-S-compliant; the predictions remain untested; the prerequisites for a proper test are now specified.

Net: the cFDT translation document and the framework spec entries about cFDT signatures should be marked as awaiting RFC-S-compliant test, not as failed predictions. (Updates landed in those documents in the same edit pass as this revision.)
