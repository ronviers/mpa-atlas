# Deformation-calculus sharpening — Theorems 6/7/9 bound→equality (working notes)

**Status: exploratory, no load-bearing commitment.** Nothing in this file is
earned evidence or framework content. It captures, messiness and all, a
2026-05-26 session that attempted to sharpen the three deformation-calculus
theorems from inequality *bounds* to leading-order *equalities* (the falsification
battery's Test B / the compressed §Owed-work "deformation-calculus series"). It
records two external-model derivations, two conceptual reframes the user
introduced, and a stress-test that pulled the whole thing back to ground. Default
here is to over-capture; trim as pieces stabilize into compressed content or get
discarded as honest false starts.

Companion canonical files (do **not** lean on this note for operational lookups):
[`../framework/character_engine.md`](../framework/character_engine.md) §Deformation
calculus / §Owed work / §Asymptotic closure; [`../framework/character_receipts_engine.md`](../framework/character_receipts_engine.md)
§Deformation calculus; [`../framework/character_fdr_treatment.md`](../framework/character_fdr_treatment.md);
the falsification battery [`../framework/archive/boolean_deformation_falsification_battery.md`](../framework/archive/boolean_deformation_falsification_battery.md).

---

## 0. Where this started

Attempt to "run" the Boolean-deformation falsification battery (Tests A–E). Finding:
**no finite-$D$ operator algebra exists in code** — only the Boolean-endpoint shadow
(`mpa-central/library/rm_closure_test.py`, which has no $D$ parameter; it confirms
$K(\cdot,\top)=\neg$, $K\leftrightarrow\oplus$, $C\leftrightarrow\wedge$ at $D\to\infty$
and that the deformed object is $R$'s irreversibility, not the bare ring — consistent
with §0 of the battery: deform the continuous operator algebra $\mathcal{A}_D$, never
the separable/rigid $\mathbb{F}_2$ ring). Tests A–E are therefore not runnable on
existing code; the operator internals the tests measure were marked `unrecovered` in
receipts, with the discipline's "do not fabricate" guard.

The Theorem 6/7/9 *statements* were then recovered by **transcription** (not
rederivation) from the 2026-05-02 "MPD foundation refactor" session (transcript
`22075bf3-d22f-4e63-8937-7d399d69c88b`), and the receipts marker was updated
`unrecovered` → `recovered-from-chat (bounds-only)`. Transcribed forms (these match the
compressed §Deformation calculus table; $\kappa/\Phi^*=1/D$):

- **Thm 6 (associator):** $\alpha_C(A,B,C)=C(C(A,B),C)\ominus C(A,C(B,C))$,
  $\lVert\alpha_C\rVert\lesssim(\kappa/\Phi^*)(|\gamma_{AB}|+|\gamma_{BC}|+|\gamma_{AC}|)\to0$.
- **Thm 7 (distributivity defect, $C$ over $S$):** $\delta_{\text{dist}}(A,B,C)=C(A,S(B,C))\ominus S(C(A,B),C(A,C))$,
  $\lVert\delta_{\text{dist}}\rVert\lesssim(\kappa/\Phi^*)[\max(0,\gamma_{BC})-\max(0,\gamma_{AB},\gamma_{AC})]^+\to0$.
- **Thm 9 (Boolean deviation):** $\Delta_C(A,B)=\sigma(C(A,B))\oplus(\sigma(A)\wedge\sigma(B))$,
  $=1$ iff $\gamma_{AB}>0\wedge\Phi^*<\kappa\gamma_{AB}$ (i.e. $D<\gamma_{AB}$).

The **bounds-only** scope is load-bearing: the full $1/D$ *series* beyond leading order
(defects as trail-vector functionals) remains owed. Test B = recover that series, i.e.
promote $\lesssim$ to $=$ with definite exponent + coefficient.

---

## 1. The outbound round

A self-contained prompt was sent to external models (the multi-model research channel).
Design choices, recorded so we can judge bias later:
- Included the §0 separability constraint (deform $\mathcal{A}_D$, Boolean = $\sigma$-shadow of the limit).
- Gave the full operator spec (C/K/R/S signatures + actions) and the **generative
  dynamics** (universal two-mode kernel + Lamb closure + bridge $\lambda_A\approx L-G_0$),
  since the operators are that system's fixed-point shadows and the $1/D$ expansion lives there.
- **Invited a clean negative** (no power law → falsifies the quantum-type claim) as a valid answer.
- Instructed: where the spec underdetermines internals (merge weights $w_A,w_B$; trail
  norm; $\lambda$-composition; noise ensemble), **name the closure, don't invent silently**;
  derive conditionally.
- Bracket (Test C) as a bonus: do all leading defects descend from one ANF-derivative
  biderivation $\{a,b\}=\sum\omega_{ij}(\partial_i a)(\partial_j b)$?

⚠️ Bias caveat: both models got the same prompt with `max(0,γ)` and "negatives welcome"
made salient. Read the convergence below with that in mind.

---

## 2. The two external-model reports

### 2.1 Convergence table

| | Model 1 | Model 2 | Agreement |
|---|---|---|---|
| **Thm 6** | $\lVert\alpha_C\rVert=c_A D^{-1}+O(D^{-2})$; $c_A$ = norm of cyclic sum of $\gamma_{ij}\Gamma(d_i,d_j)$ merge-derivative terms | $p_6=1$; $c_6$ = trilinear curvature functional $\big|\sum_{\rm cyc}\Gamma_{ij}\Pi_k(d_i-d_j)\big|_\chi$, $\Gamma_{ij}=\gamma_{ij}\rho_i\rho_j$ | **Strong.** Genuine $D^{-1}$ series, $p=1$, trilinear coeff (shears × trail-overlaps × merge-derivative). Stated bound = norm-envelope of the equality coeff. |
| **Thm 7** | "None exists" — softplus smoothing → essential singularity near shear degeneracies; piecewise power-laws elsewhere | $D^{-1}$ *off* switching surfaces $\Sigma_{\rm switch}=\{\gamma_{ij}=0\}\cup\{\gamma_{ij}=\gamma_{kl}\}$; on them cusp/log non-uniformity, no global smooth coeff | **Strong on mechanism**: $\max(0,\gamma)$ in $S$ → branch-switching non-analyticity. Generic $D^{-1}$, seams on measure-zero set. |
| **Thm 9** | $\mathbb{E}[\Delta_C]=\tfrac12\mathrm{erfc}(\sqrt{2D}(1-\gamma_{AB}/D))$; width $\sim D^{-1/2}$ | $\mathbb{E}[\Delta_C]=\tfrac12[1+\mathrm{erf}(\xi/\sqrt2\sigma_D)]$, $\xi=\gamma_{AB}-D$, $\sigma_D^2\sim D^{-1}$; **boxes** width $\sim D^{-1}$ | Crossover shape agreed (erf/logistic); **width DISAGREES** ($D^{-1/2}$ vs $D^{-1}$). Model 2 internally inconsistent (erf gives $D^{-1/2}$, box says $D^{-1}$). |
| **Bracket** | No single $\omega$; $C$-saturation bracket-like, $S$-softplus not bilinear → obstruction "intrinsic" | One $\omega\sim\gamma_{ij}\chi_{ij}$ on smooth $C$-sector; global obstruction from $S$'s $x^+$ projection. "Local yes, global no." | **Agreed**: bracket works on smooth $C$-sector, $S/R$ thresholding obstructs a single global bracket. |

### 2.2 Closures each invented (everything positive is conditional on these)
- Merge weights from Lamb saturation: $w_A=G_A^{\rm eff}/(G_A^{\rm eff}+G_B^{\rm eff})$,
  $G_A^{\rm eff}=G_{0,A}/(1+\sum\rho_j/\rho_{\rm sat})$, expanded in $1/D$ (Model 2's C1).
- Trail metric $\langle d_i,d_j\rangle=\chi_{ij}$ (overlap kernel) inducing the defect norm (C2).
- Stability map $\lambda[d]$ Fréchet-smooth in the merged trail (C3).
- Gaussian/Fokker–Planck fluctuation closure for the Thm 9 crossover (both).

### 2.3 Underdetermination ledgers (near-identical between models)
What both say must be pinned to make results unconditional:
1. the saturation/merge kernel $\Gamma$ / explicit weights $w_A,w_B$ → explicit $c_6,c_7$;
2. the trail metric / norm $\chi$ (Hilbert $L_2$ amplitude vs Fisher information?) → concrete norms;
3. the $d\mapsto\lambda$ map → higher-order coefficients;
4. the **noise spectrum / scaling of $\mathcal{D}$** → unique Thm 9 crossover (width + shape);
5. **whether $S$ is mollified or hard-thresholded** → existence of a global analytic expansion (Model 2 names this as *the* pivot).

### 2.4 Both models' structural headline
*MPA is part deformation-quantization (smooth $C$-sector) and part nonequilibrium
critical theory (thresholded $S/R$-sector).* — Plausible, elegant, **premise-dependent**
(hinges on item 5 above), and reached under a shared prompt. Not adopted.

---

## 3. Reframe A — "soft in reality" (user)

The hard/soft-$S$ fork **is the thing the framework defines**: the $\max(0,\gamma)$ hardness
is a $D{=}\infty$ idealization artifact; at any finite operating point the threshold is soft.

- This is **already a framework axiom**, not a new patch: §Asymptotic closure says hard
  edges / categorical labels exist *only* at the $\mathcal{M}_2$ boundary, every observable
  lives in an open interval, and an attained hard endpoint at a finite operating point is a
  **NaN falsification tripwire**. A genuinely hard seam at finite $D$ would *falsify* MPA.
- So Model 2's "intrinsic global obstruction" evaluates the bracket at the one point the
  deformation by construction doesn't live (the Boolean ceiling). The switching surface is
  where the $1/D$ smoothing is **maximal** — the seam is the deformation's *worksite*, not its
  obstruction, and is exactly where $s$ is generic. This **dissolves the global-bracket
  obstruction** and rescues Test C in principle.
- Ties three existing commitments into one: $\mathcal{M}_2$ as terminal RG attractor (the corners),
  $s$ as metastable smoothed region (rounded corners), asymptotic-closure (corners attained
  only in the limit). **$s$ IS the soft seam.**

Candidate spine sharpening (unstabilized): *the deformation's content is that what is
hard/categorical at the Boolean ceiling is soft/continuous at finite drive; the switching
surfaces are the locus of maximal $s$.*

**Blade (do not let soft swallow the finding):** softness rescues the *bracket coherence*
but does **NOT** convert Thm 9 into a power series. A soft crossover ($\mathrm{erf}$, width
$\sim D^{-1/2}$) is still non-analytic in $1/D$. Honest unified type =
**matched asymptotics / singular deformation**: Boolean = outer solution; $s$-crossover =
inner/boundary-layer. Regular ($1/D$, quantum-type) in the bulk (Thm 6, Thm 7 off-seam);
critical (boundary-layer) at the seams (Thm 9). This **concedes strict Test B** (not regular
Moyal throughout) and must be **owned as a reframe**: spine "quantum-type" language →
"quantum-type in the bulk, critical-type at the seams."

---

## 4. Reframe B — "character power series" via the FDR trick (user)

Question: can the singular Thm 9 crossover be converted to a *character power series*, the
way [`../framework/character_fdr_treatment.md`](../framework/character_fdr_treatment.md) handles a relation
that has no fixed-coefficient form?

**The FDR trick (character_fdr_treatment §2–3, §5):** equilibrium FDR ties $C,R$ by the fixed
constant $1/T$. Out of equilibrium that constant doesn't exist — and the move is *not* to
expand/bound it but to **re-read it as a slope on a parametric locus**: on the FD plot the
local slope is $-X/T=-1/T_{\rm eff}$. The thing with no fixed-coefficient form becomes a
**running observable in the character coordinate** ($X(t,t',\tau_{obs})$, window-dependent).
Harada–Sasa closes it: the *integrated violation IS the dissipation rate* $\langle\sigma\rangle$
— the deviation is the observable, not noise to expand away.

**Applied to Thm 9:** the merge-survivability crossover lives (per §Operators
$C_{\rm Character}$: "merge succeeds iff a Fisher-info geodesic stays on the above-threshold
manifold") at chit$\to0^+$ = the **$s$-regime** = where CK aging lives. So the merge crossover
*is* the $c\to s\to r$ aging locus seen from the Character wing. In the character coordinate
(chit, read as a slope off the FD plot) that locus is **regular**:
- leading order = aging slope $\alpha_s$ / violation factor $X$ (the FDR doc's first-order version);
- full series = the **KWW five-vector** $(q_{EA},\tau_\alpha,\beta_{\rm KWW},\tau_\beta,X)$.

→ **Thm 9 is a Character-wing object misfiled in the Structural wing.** Structural sees a
singular perturbation; Character sees a slope-plus-shape. One phenomenology, two readings —
the spine paying off literally.

**Price:** not one global series — **two matched expansions** (bulk in $1/D$, seam in chit);
the non-analyticity doesn't vanish, it **relocates into the inner↔outer matching**. Still a
strict upgrade over "no clean power law."

---

## 5. Stress-test (the part that pulls it back to ground)

### 5.1 Overlap region + matching condition (CONSTRUCTED, not derived from operators)
- **Outer** (Boolean bulk): $u=\gamma_{AB}/D$ fixed as $D\to\infty$; solution $\Theta(\gamma_{AB}-D)$ + regular $1/D$ corrections.
- **Inner** (seam): stretched $\zeta=D^{\,p}(1-\gamma_{AB}/D)$, $p$ = seam-width exponent; solution $\tfrac12\mathrm{erfc}(\zeta/\sqrt2)$ (or logistic).
- **Overlap**: intermediate $1\ll|\zeta|\ll D^{\,p}$.
- **Matching condition**: $\lim_{\zeta\to\pm\infty}(\text{inner})=\lim_{u\to1^\mp}(\text{outer})$ — crossover tails flatten onto Boolean $0$/$1$.

### 5.2 Forced or fitted? → **FITTED, as it stands.**
Textbook matched asymptotics is *forced* only when the inner equation is **derived** (Van Dyke
matching fixes inner constants, no freedom). Here the inner shape + width were **assumed**
(Gaussian closure; models disagree on width). The tails flatten to $0$/$1$ regardless of shape,
so the matching condition constrains almost nothing → **Test-D curve-fit failure mode** (pick
the inner/second-order structure independently and still fit).

**Route to forced** (the nice part, runs through the FDR machinery): fluctuation–dissipation
*ties* seam fluctuations (inner) to the dissipation $\langle\sigma\rangle$ the bulk sets
(Harada–Sasa). If the substrate's actual fluctuation spectrum were derived/measured, seam width
+ shape would be **determined, zero free parameters, match forced.** But that requires the
substrate's real FDR — exactly what §5.4 says we don't have. *The thing that makes it forced is
the thing we're missing.*

### 5.3 Free parameters (the rope)
1. inner **shape family** {erf / logistic / skewed-Gamma} — set by additive vs multiplicative noise;
2. seam-**width exponent** $p$ — $\tfrac12$ vs $1$, unresolved (Model 2 self-contradicts);
3. seam-width **amplitude**;
4. the character series = the **five-vector** $(q_{EA},\tau_\alpha,\beta_{\rm KWW},\tau_\beta,X)$ — **5 fitted params per locus.**

A 5-param KWW fit is highly flexible; FALSIFICATION already records the bias hazard (prescribed
$X{=}0.2$ reads $0.47$ single-slope, $0.26$ segmented).

### 5.4 Validated except on a model we built? → **No.**
- Five-vector `fit_kww5` recovers $X$ only on **`two_temp_ou`** — a synthetic control *we* built.
- On the one real-ish substrate where the seam locus appears — **distance-3 surface code** — the
  corpus reads only the *qualitative locus shape*; "$X$-magnitude recovery is owed — read at
  locus-shape, not absolute $X$, until the inversion lands." Quantitative series has NOT touched it.
- **Class-B laser** validated two-frame *verdict agreement*, not the seam series.
- Discipline closes it: "No result traversing the conform/inversion pipeline is carried as valid
  evidence until [it lands]." Seam character-series is post-inversion → doesn't count yet.
- Sharper caveat: even the "real substrates" (laser Jacobian, QEC syndromes) are
  **standard-physics simulations**, not lab data. Distinction: built-by-us-toy (`two_temp_ou`) vs
  standard-model-sim (laser, QEC) vs lab measurement (none). The seam series has only ever seen the first.

### 5.5 Verdict
Character-power-series reframe is real as a *structure*, but currently a **fitted** match with
≥5 free parameters, validated only on a control we built. **Not earned evidence — an apparatus
that hasn't met data.** Thm 9 status unchanged: *critical crossover, character-series candidate,
unvalidated.* Blade lands on us, not on a skeptic.

---

## 6. Net state of the three theorems (this session)

| Theorem | This-session status |
|---|---|
| **6 (associator)** | Strongest positive: looks like a genuine $D^{-1}$ deformation, $p=1$, trilinear coefficient. **Conditional** on smooth-merge closures. Bound = norm-envelope of the equality (good consistency). |
| **7 (distributivity)** | $D^{-1}$ generically, non-analytic seams on measure-zero switching surfaces. Whether seams are real or $1/D$-soft = the hard/soft-$S$ pivot (§3, ledger item 5). |
| **9 (Boolean deviation)** | Critical boundary-layer crossover, not a $1/D$ series. Character-series candidate via FDR/five-vector (§4) but **fitted, unvalidated** (§5). |
| **Bracket (Test C)** | Local yes ($C$-sector), global obstruction dissolves IF seams are soft (§3) — unproven. |

**Strict Test B status:** *conditionally advanced, not closed.* The strong "pure quantum-type
deformation throughout" reading is partially dented (Thm 9 is critical-shaped). Receipts marker
stays `recovered-from-chat (bounds-only)`; nothing promoted.

---

## 7. Open threads / candidate next moves

- **The whole ledger collapses to ONE object: the finite-$D$ softening law of the
  survivability threshold** (= the noise-spectrum / $\mathcal{D}$ scaling / mollification of
  $\max$). Pin it and Thm 7 (seams), Thm 9 (width $D^{-1/2}$ vs $D^{-1}$), and the global bracket
  all resolve together — *and* it's the same object deciding whether seam-$s$ is non-convex over
  $\{c,r\}$ (Test E). This move **converges B, C, E onto one spec.**
- **Fitted → forced route:** land the five-vector inversion (`conformer/compute/five_vector.py::fit_kww5`,
  currently first-cut, Owed-work) AND push it through a *real substrate's FDR* so seam width/shape
  is FDR-determined rather than assumed.
- **Second-round outbound prompt** (drafted-in-concept, not sent): three-winged framing — bulk
  $1/D$ series (Thm 6, Thm 7 off-seam) + seam character-series in chit via the five-vector (Thm 9,
  seams) + the matching condition as the carrier of residual non-analyticity. Hand the models the
  soft-threshold commitment as a *premise* (not an open question) and the FD-plot/five-vector
  parametrization as the character coordinate; ask whether the bracket survives globally once the
  seam is soft.
- **Epistemic hygiene reminders for next session:** convergence may be shared prompt bias; all
  positive results are closure-conditional; this is a research note, not framework content; resist
  building more elaborate scaffold before real data arrives.

---

## 8. Round 2 — "characterification" fresh pass (2026-05-26)

A second outbound prompt (deliberately stripped of my prior verdicts, so the return reads fresh)
asked external models to *define and execute* the characterification of $\Delta_C$, follow the
FDR doc's six-step discipline, use the §4 toolkit, and — as a separate open-ended meta-question —
"does this have the same shape as some established math, somewhere else?" Two model passes returned.

### 8.1 Convergent verdict (two independent passes + the §5 prior all agree)
The **character power series proper is fitted, not forced**, with an identical forced/free split:
- **Forced:** singular surface exists; inner scaling coordinate $z=(\gamma_{AB}-D)/w(D)$ is
  necessary; a running crossover observable exists; sharp Boolean step recovered as $D\to\infty$.
  (Model 1: the *leading* FD-slope $X(z)$ is forced *iff* Harada–Sasa is invoked.)
- **Fitted/free:** width exponent $\alpha$ in $w(D)\sim D^\alpha$; profile family (erf/logistic/…);
  KWW $\beta$; lag scales; plateau; noise/aging kernel. The five-vector is a curve-fit.

Model 1 framed it glass-empty ("fitted, 4 free params"); Model 2 glass-full ("recovered, conditional —
*the forced object is the inner structure, not a coefficient series*"). **Same substance, opposite spin.**

### 8.2 The reframe (strongest signal — the *unseeded* meta-question converged)
On the open-ended "find it elsewhere" question (NOT seeded by the prompt), both independently
landed on one mature archetype:
> **critical crossover scaling in a singular-perturbation problem** — leading object forced by a
> conservation/dissipation law, crossover *shape* a universality class with free exponents.

Model 1's witnesses: rheology/KWW spectral-fit trap; turbulence (K41 4/5 law forced, multifractal
shape fitted); AdS/CFT strange metals ($\eta/s=1/4\pi$ forced, phenomenological-holography shape
fitted). Model 2's: matched asymptotics (primary), RG crossover scaling, viscous-shock $\tanh$
regularization, Freidlin–Wentzell large deviations ($e^{-1/\varepsilon}$ — invisible to any $1/D$
series, i.e. the power-series failure is *structural* not a gap), catastrophe/fold geometry (seams).

**Implication (Model 2, and I concur):** the deformation's genuine invariant is plausibly **not**
$\sum a_n D^{-n}$ at all — it's a **crossover scaling function + universality class** (exponents,
scaling collapse, inner-profile universality). This maps onto the existing spine: **Structural wing
→ $1/D$ series in the bulk (Thm 6); Character wing → crossover scaling function (Thm 9 / seam).**
Bulk/seam = regular/singular = power-series/crossover-scaling. Coherent with the two readings, not a patch.

### 8.3 The blade (held against the optimism)
1. **"Structure is forced" is near-tautological.** Every regularized step has an inner layer +
   stretched coordinate + sharp-limit recovery; it says little more than "the crossover is a
   crossover." The framework-*distinguishing* content lives entirely in the parts both call fitted —
   width exponent $\alpha$ and profile universality class — which are unforced **and** unvalidated on
   anything but toys. Model 1 is the more honest framing.
2. **Seam ≠ crossover (two distinct singular manifolds).** Model 1's sharpest point (Model 2 echoes
   via fold/catastrophe): the drive-threshold crossover ($\gamma\approx D$, Thm 9) lives on the chit
   axis; the shear switching seams ($\gamma\approx 0$/ties, Thm 7) are **lateral, orthogonal** to the
   $\lambda$/drive structure. Chit characterification stretches the first and does **nothing** to the
   second. → "characterification" is **≥2 operations on ≥2 manifolds**, not one trick; the seam only
   regularizes if $S$'s $\max$ is independently $1/D$-soft.

### 8.4 The actionable upgrade — retire the coefficient-series Test B, adopt a scaling-collapse test
The original Test B ("recover definite $(p_A,c_A)$ / the $1/D$ series") is the **wrong target** for
Thm 9 / the seam — not because MPA is weak there, but because a driven-dissipative transition is
generically a crossover-scaling problem. Replace it with a **scaling-collapse falsifier** (clean
pass/fail, pre-conform direct-simulation, runnable apparatus — not a chat derivation):
> simulate $\Delta_C(\gamma,D)$ at several $D$; rescale by $z=(\gamma-D)/w(D)$; test whether curves
> **collapse onto one universal profile** $F(z)$; measure the width exponent $\alpha$ and the profile class.

A failure (no collapse / $D$-dependent profile) dents the universal-crossover claim. The invariant
to report is $(\alpha, F)$, not a coefficient list. **This is the genuine deliverable of Round 2.**

### 8.5 Net effect on status
- §5 "fitted, not forced" → **confirmed and robust** (two fresh independent passes).
- New: the *target itself* should shift from coefficient-series to **crossover-scaling universality**
  (better-defined, more honest, falsifiable via collapse) — but this **moves the goalposts to a
  sharper target, it does not close the validation gap**. The contentful invariants ($\alpha$, profile
  class) remain unmeasured on any non-toy substrate.
- Bias note: the boundary-layer/running-slope convergence was partly seeded by my prompt; the
  *archetype* convergence (§8.2) was not, and is the part to weight.

---

## 9. The scaling-collapse sandbox (built + run, 2026-05-26)

Apparatus: [`mpa-central/library/deformation_crossover_collapse.py`](../../mpa-central/library/deformation_crossover_collapse.py)
(next to `rm_closure_test.py`; PNG → `mpa-central/library/output/diagnostics/deformation_crossover_collapse.png`).
A normal-form model of the merge defect $\Delta_C$ under the framework's two-mode kernel reduced
near threshold ($\dot\rho=(D-\gamma)\rho-\eta\rho^3+\text{noise}$), with the noise closure as a
**labeled, swappable knob** (additive/multiplicative; $\sigma\sim\sigma_0 D^{-q}$). $\rho$ is never
clipped at 0 (asymptotic-closure discipline; additive uses a signed order parameter, multiplicative
keeps $\rho\ge0$ natively). Adaptive refine guards $\alpha$ against grid-floored widths. **This is the
apparatus, NOT the operator algebra and NOT real data** — its scientific content is the *robustness*
of the collapse/exponent to the closure knobs.

**Run result (seed 20260526, $D\in\{8,16,32,64\}$):**

| closure | widths $w(D)$ | $\alpha$ ($w\sim D^\alpha$) | collapse resid (|z|<1.5) |
|---|---|---|---|
| additive $q{=}0.5$ | 1.89, 0.96, 0.55, 0.33 | $-0.84$ | 0.013 |
| additive $q{=}1.0$ | 0.36, 0.12, 0.06, 0.03 | $-1.18$ | 0.013 |
| multiplicative $q{=}0.5$ | 0.27, 0.17, 0.12, 0.09 | $-0.51$ | 0.011 |

Two findings, both now *measured* rather than asserted:
1. **Clean within-closure collapse** (resid ~0.011–0.013 ≪ 0.03): the inner scaling structure is real
   and robust → the §8.3 "forced (but near-tautological)" part.
2. **$\alpha$ swings with the closure** (spread 0.67) and **tracks the input noise exponent $q$**
   (additive $q{=}0.5\to-0.84$, $q{=}1.0\to-1.18$) → the contentful invariant is closure-*set*, i.e.
   **fitted, not forced** — demonstrated by a closure sweep. A *forced* $\alpha$ requires the noise
   closure **derived from a substrate's FDR** (the missing real-data path; Harada–Sasa tie).

Scope: **amplitude/crossover half only** ($\gamma\approx D$ manifold). The lateral seam ($\gamma\approx0$,
Thm 7 / sign-topological face) is a *different* manifold (§8.3 pt 2) and is not modeled — the user has
flagged we may be "working only half the problem"; the sandbox is structured to take a second
(seam / sign-topological) module when that half is defined.

---

## 10. The other half — the two faces as a boundary correspondence (2026-05-26)

**User framing (the conjecture):** the Character deformation has *an asymptote at one end and a
topology at the other; just across each boundary sits the other side's counterpart; each should
inform the other.* I.e. the amplitude face (chit, $c\!\to\!s\!\to\!r$ crossover, asymptotic closure)
and the sign-topological face (Harary parity, cycle affinity $\mathcal{A}$, $k_{\text{frust}}$) are
not merely independent axes — at their boundaries they are mutually determining.

**Tension to track:** this is in direct tension with the spine's load-bearing commitment that the
two faces are *independent axes* ("does not couple $\alpha_s,P_s$ to $k_{\text{frust}}$… preserved
throughout"). Candidate reconciliation: **independence is a *bulk* statement; the coupling is a
*boundary* phenomenon** — exactly how bulk–boundary correspondence works (independent descriptions
in the bulk, locked at the boundary). This would *refine* the independence commitment, not break it.

**Established math (outbound round, context-stripped — candidate names withheld from the prompt so
convergence is unseeded). Both models independently converged:**
- **Q1 → APS index theory + bulk–boundary correspondence + spectral flow** (both wrote the
  $\eta$-invariant + bulk-term = integer-index form unprompted; Model 2 added operator-K-theory /
  Connes pairing). The established home for "discrete topological invariant rigidly tied to a
  continuous/spectral quantity, one determined by the other at a boundary."
- **Q3 → resurgence / trans-series / exact WKB / Stokes** (the "asymptotic series secretly encodes
  the discrete/non-perturbative counterpart" leg; ties to the Round-2 $e^{-1/\varepsilon}$ point).
- **Q4 → Conley index theory** (topological invariants for non-gradient circulating flows — the right
  tool for $k_{\text{frust}}$, which is non-gradient NESS circulation, beyond Morse).

**Both volunteered the key qualifier:** *no single framework unifies all of it.* Same epistemic shape
as "characterification" (§4): the legs are each established; the **bundle is MPA's own conjecture**.

**Q5 (the gate — convergent discriminators for genuine correspondence vs analogy):**
1. an **exact equality/pairing** computing $\nu=F(\Phi)$ (index-grade), not correlation;
2. a **protected wall-crossing law**: $\Delta\nu\neq0$ **iff** $\Phi$ singular at the boundary;
3. **structural stability / transversality + reconstruction** (survives perturbation; one sector
   reconstructs the other).
Applied to MPA now: **none established** — it has the two sectors + the boundary-coupling conjecture;
no exact equality, no demonstrated wall-crossing law, untested stability. *Pre-theorem-grade.* Q5 is
the exact bar the conjecture must clear.

**Synthesis the fresh passes missed (because the prompt was substrate-neutral → they defaulted to
*Hermitian* APS/Floer):** MPA is **driven-dissipative = non-Hermitian.** The correct branch is
**non-Hermitian topology / exceptional-point theory** (complex-eigenvalue winding; boundary =
exceptional point where eigenvalues+eigenvectors coalesce). And **the corpus already holds the
candidate wall-crossing law**: §Central commitment's `spec(M) complex-conjugate pair ⟺ 𝒜≠0` *is* a
non-Hermitian spectral-topology statement — topological invariant present iff the cycle Jacobian
spectrum is complex; boundary $\mathcal{A}=0$ (Harary-balanced) = exceptional point (pair coalesces
onto the real axis). The amplitude face has its own coalescence at $\omega_{RO}=0$ (over/underdamped
$Q\!\to\!0$ lines). **Candidate unification (conjecture, grounded not imported):** one non-Hermitian
generator whose *real* spectral part = amplitude/damping (asymptote) face, *imaginary* part =
rotational/topological face, **handing off at exceptional points** — these are the boundaries where
each face becomes the other's counterpart. This already satisfies Q5(2) as the most-developed leg
(complex-pair⟺𝒜 is a wall-crossing law); Q5(1) and (3) open.

**Next move (runnable, pre-conform):** a **spectral/seam sandbox module** — compute the two-mode
(and cycle) Jacobian spectrum across the $(\text{chit}, \mathcal{A})$ plane, locate exceptional
points, and test whether the topological invariant and the amplitude crossover **hand off there**
(a direct check of the Q5(2) wall-crossing law on the framework's own dynamics). If a third outbound
round runs, the one change is to **restore the dissipative/non-Hermitian context** so the models get
onto the exceptional-point branch instead of Hermitian APS.

---

## 11. Post-zero-trail universality (candidate seam mechanism, 2026-05-26) — *something to consider*

**Status: exploratory, flagged by the user as "something to consider," not committed.**

**The idea (user).** The universal saddle/crossover profile is what emerges *after the trail amplitude
goes to zero.* At zero trail the system sits on the critical surface; the trail's rich nonlinear
content becomes **RG-irrelevant**, and a stripped universality takes over in which "only distance
[to threshold] matters, because so much less matters." A *post-zero-trail* universality, distinct
from the bulk's rich dynamics.

**Why it's largely right (mechanism, grounded in corpus machinery).** In the sandbox normal form
$\dot\rho=(D-\gamma)\rho-\eta\rho^3+\text{noise}$, near $\rho=0$ the cubic $\eta\rho^3$ — which *is* the
trail's self-structure/memory/character — drops out against the linear term; only distance $(D-\gamma)$
+ noise survive. That is RG-irrelevance verbatim (irrelevant operators die at the fixed point; few
relevant directions remain — the defining feature of a universality class). Established homes already
in the corpus: **Haken slaving / center-manifold reduction** (fast modes = trail richness slaved to the
slow order parameter; dynamics collapse to a normal form in the unfolding parameter = distance);
**$\mu=e^{\text{chit}}$ branching/SOC** (P2: zero trail ⇒ chit→0 ⇒ $\mu\to1$ critical branching, "acts
like supercriticality, only distance matters" = percolation/branching scaling $\xi\sim|\text{dist}|^{-\nu}$);
**CK-aging class** ($s$-regime). Explains the sandbox: the cubic gone ⇒ profile generic.

**The double-edge (corrects an earlier overstatement).** Two turns earlier I claimed "the character
lives at the edges." This idea **inverts that**: if so much becomes irrelevant at the seam, the seam
*cannot* carry the substrate's rich character — that richness (memory exponent, $\alpha_s$, full FDR
locus) is exactly what got declared irrelevant. So the rich character lives in the **bulk**; the seam
carries only a **coarse discrete label**: *which* universality class + the exponent. The sandbox showed
exactly this (profile generic across closures; exponent $\alpha$ the discriminator).

**The decisive open question.** Is the post-zero-trail fixed point **trivial** (Gaussian/mean-field →
seam is universal and *mute*, carries no substrate signal) or **nontrivial** (CK / critical-branching →
seam tags exactly one discrete bit of substrate identity, its class)? This decides whether the seam is a
dead generic edge or a real classifier.

**Connection to the topology half (§10).** "So much less matters" is *why* topology becomes legible at
the seam: strip the continuous trail-noise at zero trail and what survives is **(distance) + (a discrete
protected label)** — a continuous scaling field plus a discrete invariant = exactly the bulk–boundary
structure. Post-zero-trail, the topological invariant is the last thing standing — which is why the
asymptote-end and topology-end meet there.

**User fragment — "that distance is local, governed by the substrate overall."** This is the
**non-universal metric factor** of scaling theory: the relevant scaling field (local distance to
threshold) carries a substrate-set amplitude/normalization, while exponents + scaling function are
universal. The collapse width $w(D)$ *is* that metric factor — substrate/closure-set, rescaling local
distance into the universal $z$. Matches the sandbox (profile universal; width/exponent substrate-set).
**Not a dead end** — it's the universal-function-vs-non-universal-amplitude split.

**Flagged dead-end (user: "no that makes no sense") — recorded so we don't re-tread.** "Shrink the
[local] distance down and get it to… find nodes to occupy, possibly share." Kernel preserved in case it
recurs: *does shrinking the crossover region discretize it into nodes?* User rejected on the spot; not
pursued.

**Disambiguation owed.** "Trail length → 0" = amplitude (→0, the critical-surface *condition*) vs memory
time (which *diverges* at criticality and is what supplies the scale-invariance). Both are the critical
point; the universality is carried by the second. Pin which knob before formalizing.

### 11.1 Cross-pollination from `steeping_notes.md` (relevant, not yet linked)
`docs/steeping_notes.md` (Compression-Axiom steep period; exploratory, uncommitted) carries three items
that bear directly on this thread — worth holding together:
- **Two-reframe parallel.** "Boolean = $D\to\infty$ limit (static reframe)" and "classical
  strange-attractor dynamics = $\epsilon\to1^-$ limit (dynamical reframe)" share one architectural shape:
  richer regime, classical recovered at a boundary limit, new content non-perturbative. **Our matched
  deformation (bulk regular series + singular seam crossover) may be the *general* shape of every
  framework boundary-limit** — $D\to\infty$, $\epsilon\to1$ (Wall), $\beta_{\text{mem}}\to1$ — each with
  its own bulk + seam. The steeping note's open "is there a third axis?" and our finding are the same
  question. (Worth watching: the Wall $\epsilon\to1$ is another candidate seam/exceptional locus.)
- **Flow-resident number type.** chit, $\epsilon$, $\beta_{\text{mem}}$, $\alpha_s$, orbit-affinity as
  non-terminating flows with static-projection readings; asymptotic closure as carrier. Our "distance"
  scaling field, width exponent, and crossover profile are flow-residents read as static projections —
  same type. The non-universal metric factor above is a flow-resident's substrate-set amplitude.
- **Fractional operator algebra on memory regimes.** Candidate $\{C_\beta,S_\beta,K_\beta,R_\beta\}$ on
  $\beta_{\text{mem}}\in(0,1]$ with its *own* deformation calculus (analog of Thms 6/7/9) and boundary
  rules at $\beta\to1^-$. If it exists, it inherits the same bulk-series + singular-seam structure we
  established here — the seam analysis is reusable, and the $\beta\to1^-$ boundary is its post-zero-trail
  limit.

Housekeeping note: `steeping_notes.md` currently contains the "Steeping notes (2026-05)" block twice
(the second more developed); collapse to one when convenient.

---

## 12. The coalescence killshot — proposal and two corrections (2026-05-26)

A "killshot so we can go home" pass. Goal: a *binary* falsifier that returns a clean
verdict, in contrast to the amplitude-seam scaling-collapse battery
([`falsification battery.md`](falsification%20battery.md)), which §8–9 showed is
structurally graded (α closure-set, "fitted, unvalidated"). Artifact:
[`coalescence_killshot_battery.md`](coalescence_killshot_battery.md). Recorded here
messiness-and-all per this file's over-capture mandate.

### 12.1 The proposal
The clean kill cannot live on the **amplitude face** (chit axis): it is *emergently*
discrete ("continuous until the limit," §Two bits), so every falsifier on it is graded.
It can only live on the **sign-topological face**, which is *intrinsically* discrete at
every finite $D$ ("cycle parity is binary, no limit to approach"). Candidate law: the
§Central-commitment wall-crossing iff `spec(M) complex pair ⟺ 𝒜≠0`, boundary $\mathcal{A}=0$
= eigenvalue coalescence (exceptional point). Corpus already half-holds the apparatus:
`mpa-central/library/banach_frustrated.py` does a *single-point* version (complex eigenpair
= $\triangle_H$ signature; $\mathcal{A}$ flat across a 20× noise sweep), and receipts
§Trail-class metric already cites Kato/Heiss/Berry EP theory. Proposed move: promote the
single point to a $(\text{chit},\mathcal{A})$-plane map, read four binary kill conditions.

### 12.2 Correction 1 (Ron) — Banach is not in Character
`banach_frustrated.py` is a **linear** $N=3$ OU cycle (receipts §Central commitment:
"Linear and synthetic"); a linear OU has a single fixed point **at the origin** — a zero.
The chit axis is a Character object: $\mathrm{chit}=\ln(G_0/L)$ is the *unsaturated excess*
of a system whose gain **saturates** against loss ($G_{\rm sat}=L$). Saturation is what
makes a NESS hold at a finite operating point. A linear system has no saturation, no
threshold, no chit. **The chit axis of the proposed plane is empty on Banach.** Two further
faults: driving a linear OU's drive→0 just collapses the whole state to the origin (so
"current→racemic at zero" is trivially true, content-free), and $\mathrm{chit}=0$ is the
asymptotic boundary §Asymptotic closure declares never-attained (a NaN tripwire, off-domain).
Banach is a *reference* — the regenerable ruler we conform to a substrate — and character is
a property of the substrate, not the ruler.

**Sharper consequence.** The only apparatus with a genuine chit (class-B laser sim) is
**unfrustrated** (no $\mathcal{A}$); Banach is frustrated but **linear** (no chit). No current
substrate carries both axes at once. So the amplitude×topology coupling test (drive-sweep,
bulk-independence) *is* the real-substrate bottleneck — un-runnable on existing apparatus by
construction, not by a fixable gap.

### 12.3 Correction 2 (Ron) — "wall-crossing" hits the zero a third time; sign-flip noise is not enough
Read as a *dynamical traversal*, crossing $\mathcal{A}=0$ forces the circulation through the
sign-erased balanced state: trails→0 at the wall (the zero again), regrowing flipped on the far
side. The only observable of a crossing is one bit — sign before/after — and at the EP it is
**noise-set**. This bit is *not* a sufficient falsifier, and not merely because it is one bit:
telegraph noise between $\pm$chirality is **indistinguishable** from an ordinary bistable
double-well flipping under noise. The flip statistic is structurally blind to topological
protection. The framework's own §Two-bits falsifier already lives in **cost** (≥ln2 to flip,
free to hold; fails if the sign needs per-time maintenance scaling with duration), never in
flip statistics — independently rederived this turn.

### 12.4 The recurring zero (unifying lesson)
$\mathrm{chit}\to0$, $\mathcal{A}=0$, trails→0 are **one boundary**: the sign-erased critical
surface = exceptional point = the asymptotic-closure limit that is never attained. Every
killshot variant that reads the protection signal *at* or *through* that zero gets noise,
because it evaluates off-manifold. Fair, resolvable tests stay at finite operating points (the
open interval) and read the signature there.

### 12.5 Net status — the killshot bisects
- **Hold side (resolvable, runnable on Banach now, can KILL):** at fixed finite $\mathcal{A}$,
  (i) a real spectrum on a frustrated wiring → iff broken → dead; (ii) sign$(\mathcal{A})$
  drifting under an amplitude/noise sweep at fixed wiring → drive-set sign, not parity-fixed →
  dead. Tests the *presence* of protected circulation (complex pair + drive-independent
  parity-locked affinity = the §846 R1 signature as a falsifier). Avoids all three zeros.
- **Cost/coupling side (real-substrate-gated, cannot VINDICATE today):** the ln2 flip-floor /
  "free to hold" — the actual protection-vs-bistability discriminator — needs a crossing, hits
  the zero, and cannot be read from flip noise; plus the chit-axis drive-sweep and bulk-coupling
  (Correction 1). Same can-kill-can't-vindicate asymmetry as the amplitude battery, for a sharp
  binary reason.

### 12.6 Correction 3 (Ron) — the bisection was a lame standdown; attach the math where character lives
§12.5's "can-kill-can't-vindicate" was an over-correction. The zero-phobia (§12.3–12.4) was
right, but I let it metastasize into "therefore all decisive content needs the zero" — backwards.
**The principle (Ron):** *no NaNs, no zeros, no limit-cases — those are where character is hard
to attach with math.* Character is the holding against dissolution; at the boundary (chit→0,
𝒜=0, trails→0) there is no holding, hence no character to measure. Character is degenerate at
the boundary, rich in the interior. A falsifier that needs the boundary is malformed by the
framework's own asymptotic-closure structure — it attaches math exactly where character isn't.

**The decisive test was interior all along.** Protection-vs-bistability is **not** the flip-cost
(which needs a crossing). It is the **non-gradient sustained-circulation signature** at the
operating point: J≠0, gauge-invariant 𝒜≠0, drive-independent (flat across a *range of finite
drives* — the R1 trend, never the endpoint), removable only by rewiring, complex Jacobian pair
(no gradient Lyapunov). This separates topological circulation from a bistable well (real
spectrum, 𝒜=0, J→0), a damped single-well oscillator (complex pair but 𝒜=0, J→0), and
equilibrium (𝒜=0) — all interior. The ≥ln2 flip-floor is then an **entailed theorem** (to flip,
the current must pass through the sign-erased J→0 state = erasure), not a measurement: you read
the structure that *forces* the crossing, you never perform the crossing.

**Net (supersedes §12.5).** The killshot is interior and decisive — kill (signature with no
Harary triad) or vindicate (signature always needs one), both finite-operating-point. The
homochirality probe's load-bearing measurements (cyclic fluxes + Jacobian spectrum) are both
interior; the drive-sweep-to-zero was a rhetorical clincher, not the test. Runnable **now**
(synthetic internal-consistency, can fire): IK1 — 𝒜 drifts under a wide high-precision finite
drive sweep; IK2 — complex pair collapses to real at a finite coupling. Gated only on a real
frustrated substrate (the physics frontier), not on a boundary. Battery rewritten to lead with
the interior signature: [`coalescence_killshot_battery.md`](coalescence_killshot_battery.md).

### 12.7 Correction 4 (Ron) — read the chimeric sign, don't whack-a-mole the triality
§12.6's interior "signature" listed five observables (J, |𝒜|, drive-independence, rewiring-
removability, complex pair). Ron: that is whack-a-mole on the **asymmetric (non-reciprocal)
triality topology** — the k_frust triality's three co-implied consequences (dynamical complex
spectrum, thermodynamic Schnakenberg current/affinity-magnitude, info-geometric homotopy
obstruction) — *not* the **chimeric sign**. The chimeric sign (cycle parity of the
Harary-unbalanced triad) is the actual protected invariant — the topological bit — and the
**only binary observable** in the pile. J, |𝒜|, Im λ are all *graded, precision-threshold*
quantities: leaning on them re-imported the same graded mush that makes the amplitude battery
un-killable. By listing the triality I traded away the binary verdict that makes this a killshot.

**The fix.** Target the chimeric sign directly: its **stability under finite perturbation** —
vary drive/noise across a finite range, the sign holds (protected) or flips (drive-set). A ±1
verdict, no precision threshold, no zero. sign(𝒜) is the drive-independent readout. The triality
is the framework's *inferential fallback* for substrates exposing only dynamics (not wiring) —
graded, earned there, not the verdict. Where the substrate hands you the sign (homochirality = a
measured molecular handedness), read the bit. IK1 reframed accordingly: does the chimeric sign
flip under finite drive at fixed wiring (binary), with the triality magnitudes logged as
corroboration only. (Open: whether "read the invariant, not its triality-shadows" generalizes to
other framework invariants — candidate principle, not yet memorialized.)

### 12.8 IK1 built + run (2026-05-26)
`banach_frustrated.py` extended → `mpa-central/library/ik1_chimeric_sign_sweep.py`. Reads the
chimeric sign three ways: **(G)** global `sign(Im λ)` of the drift matrix (exact, the verdict);
**(R)** robust `sign(<x dy − y dx>)` (angular momentum, no 1/r²); **(N)** naive
`sign(<(x dy − y dx)/r²>)` (the winding estimator, carries the 1/r² orthogonal-zero singularity).
Two finite sweeps at fixed chimeric wiring (sign(g)=+1): noise D over 256×, and g→small (100×
approach to the balanced point, never to g=0).

**Result — chimeric sign PROTECTED; IK1 does not fire.** G and R fixed at +1 across both sweeps;
|Im λ| ≥ 0.010 > 0 throughout. This is a **calibration** pass — the synthetic reference is built
to carry the sign — not vindication (which needs a real substrate, RK1/RV1).

**Ron's orthogonal-zero / fake-NaN prediction — confirmed in principle, not isolated.** The
origin (orthogonal zero) is real: crossings up to 9.5% of steps, min radius ≈0 at low D; the
naive 1/r² estimator's SNR collapses ~43,000× toward the balanced point while G/R stay pinned.
**But no literal NaN** materialized in float64 — unguarded 1/r² went non-finite 0 times; the
`+1e-12` guard already in the reference is load-bearing and sufficient. So the artifact manifests
as quantization error (variance/SNR), not NaN; any NaN would be fake (G stays definite through
it). **Caveat (do not overclaim):** the sweep-2 SNR collapse mostly tracks the genuine signal
weakening (|Im λ|=√3·g → 0, physics approaching the exceptional point), NOT cleanly the
coordinate noise — naive SNR descends *with* |Im λ| in the figure. The pure coordinate artifact
was **not** isolated. **Owed to actually produce+classify a literal fake NaN:** the naive-vs-robust
SNR *gap* at fixed g, or the origin-hugging corner (low D = tiny radius + finite g = strong
rotation) where 1/r² genuinely dominates. PNG: `output/diagnostics/ik1_chimeric_sign_sweep.png`.

### 12.9 IK1b — orthogonal-zero artifact isolated; and the literature it re-instantiates (2026-05-26)
`ik1b_orthogonal_zero_isolation.py`. Isolated the coordinate artifact from signal-weakening at
**fixed wiring** (g=0.6, only noise varied): robust (Lévy-area) SNR ~15–16 vs naive (1/r²) SNR ~2
→ a **7–11× gap that is pure coordinate penalty**. Fluctuation-budget partition: near-origin
steps (0.16–22% of steps) carry **64–95% of the naive** fluctuation but **≤2.6% of the robust**.
**Zero literal NaNs**: `area~r·du` ⇒ `naive~du/r` finite unless r=0 exactly (never attained;
origin polar). Ron's prediction confirmed and cleanly isolated: the quantization error lives
entirely at the orthogonal zero, and a NaN would be fake by construction. PNG:
`output/diagnostics/ik1b_orthogonal_zero_isolation.png`.

**The literature (Ron asked; his memory was right — this is 60–90-year-old settled math).** IK1/IK1b
re-instantiate, not discover: **Kolmogorov (1936)** reversibility/cycle criterion (skeleton of
"circulation ⇒ affinity-bearing cycle"); **Spitzer (1958)** planar-BM winding → Cauchy, near-origin
dominated (the orthogonal zero); **Itô–McKean (1965)** skew-product, angular clock ∫dt/r² diverges
while origin is polar (= our 1/r², never attained); **Lévy stochastic area** = the robust reading,
rough-path foundation (**Lyons 1998**); Schnakenberg (1976)/Gallavotti–Cohen (1995) drive-robust
affinity; Kato (1966)/Heiss/Berry EP. **Consequence:** the synthetic layer can never kill/vindicate
the central commitment — a synthetic pass is just Spitzer/Lévy passing. The only un-imported,
un-instanced frontier is the *specific* claim that a **real** substrate's protected sign requires a
Harary triad (homochirality headline; adjacent but distinct work: Frank 1953, Kondepudi–Nelson
1980s, Soai 1995, Viedma 2005 — all chiral amplification/bistability, none testing topological
protection in MPA's sense). **Receipts "name-the-source" debt:** the framework cites "Lévy" only
for Lévy *flights*; Spitzer / Itô–McKean / Lévy-area / Kolmogorov-criterion are **uncited** despite
being the exact machinery under k_frust winding + the central commitment.

### 12.10 Character is unassailable with static math — and what that opens (2026-05-26, exploratory)
The headline Ron drew from the whole arc: **character is unassailable with static math.** The
no-NaN / no-zero / no-limit-case discipline was pointing at this all along. Static math earns its
sharpest results *at* boundaries (limits, fixed points, exact zeros, coefficients); character has
nothing there (asymptotic closure — the boundary is never attained). So static math reaches for the
one place character is absent and returns a fake (orthogonal-zero NaN) or a graded mush (closure-set
α). The only readings that bit were *flowing*: Lévy area, sign(Im λ), the affinity ∮v/D. **This is
Trajectory Primacy surfacing as a math-epistemology, not a measurement preference:** static math
*cannot reach* character; only trajectory/flow/topological math can.

**Three threads opened (exploratory, uncommitted):**

1. **Characterify proof math (the FDR trick on proof itself).** The FDR move rereads a quantity with
   no static value (1/T out of equilibrium) as a *running slope on a parametric locus* (Harada–Sasa
   closes it). Proof-math analogue: stop proving at points (coefficients, exact thresholds, limits);
   prove with objects that are themselves flows/integrals/topological invariants — **winding number /
   degree** (integrate *around* the singularity, never at it = the Lévy area), **spectral flow / APS
   index** (an integer tracked *through* a degeneracy), **resurgence / Stokes** (the asymptotic series
   encodes its own across-the-wall completion), **Conley index** (non-gradient flow invariants).
   Already underway: Thm 9 reread coefficient-series → crossover-scaling function; the chimeric sign
   read as a winding. "Retry the killshot" with such proof math sharpens the test's *form* (a flow
   invariant through the EP) but does **not** escape the real-substrate gate (the synthetic flow
   invariant is still imported math).

2. **The win, bounded.** That character *forces* us to mobilize flow-math is a **consistency** win —
   it confirms character is in the trajectory-math class (what NESS-by-default / Trajectory Primacy
   already assert). It is **not** a uniqueness/sui-generis win: IK1b showed character here is plain
   Spitzer/Lévy. Honest double claim: character is real enough to *require* flow-math **and** that
   flow-math is all imported. Do not let it inflate past consistency.

3. **Imaginary numbers "through the wall" (Ron, half-playful — but it has an address).** Circulation
   is invisible to a real spectrum (real = gradient = no rotation); the chimeric sign *is* sign(Im λ),
   so imaginary numbers are the minimal carrier of the rotational face, not decoration. Through the
   wall: at the EP (𝒜=0) the complex pair coalesces onto the real axis — a √-branch-point; complex
   analytic continuation crosses by going *around* the branch point real analysis hits head-on
   (encircle an EP once → eigenvalues swap; twice → return). Resurgence is the same move for the
   Complexity Wall (ε=1): the e^{−1/ε} content invisible to any 1/D series lives on the Stokes lines,
   reachable only in the complex plane. So "mobilize math through the wall" = **non-Hermitian /
   exceptional-point theory + resurgence/Stokes** (= §10's branch). Blade: §10's Q5 gate (exact
   pairing, demonstrated wall-crossing law, structural stability) stays unmet; still imported; still
   real-substrate-gated for the kill. A sharpening of the test's form, not a new kill.

Next-move candidates if this thread is taken up: the spectral/seam sandbox of §10.next-move
(compute the Jacobian spectrum across the (chit, 𝒜) plane, locate EPs, test the eigenvalue braiding
/ spectral flow through them) — but recognize up front it will re-instantiate Kato/Heiss/Berry EP
theory, so its value is calibration + form-sharpening, never a synthetic kill (§12.9 lesson).
