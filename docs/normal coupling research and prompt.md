
> **I'm studying a population of coupled noisy nonlinear oscillators, each of which carries a directed cyclic current (a nonequilibrium steady-state circulation), and I want to characterize the *drive* — the nonequilibrium budget that sets the circulation — separately from the topological/structural invariants of the circulation. I want to know where the established literature already owns this decomposition, the right names/theorems, and where my framing is loose or wrong. Please answer with specific named results and citations.**
>
> **SETUP.** A single *unit* is a noisy nonlinear oscillator whose steady state carries a directed cyclic current in its state space — concretely a 3-state cyclic Markov process, or a 3-variable rotational flow (Stuart–Landau-like) with a stable focus or limit cycle. Each unit has:
> - an **orientation**: the rotation axis / sign of the winding (the chirality), equivalently the **sign of the cycle affinity** (the thermodynamic force around the loop). For a cyclic (circulant) coupling this axis coincides with the unit's slow / Perron eigenvector. It is a discrete (topological) invariant.
> - a **magnitude**: the size of the steady-state cyclic current ("flow rate").
>
> I drive each unit out of equilibrium (noise amplitude / chemical-potential difference / energy budget). Empirically, in the linear (Ornstein–Uhlenbeck) regime the **cycle affinity** (the log-ratio of forward/backward rate-products around the loop) is **independent of the drive amplitude** — it is set by the coupling structure — while the **current magnitude** scales with the drive (∝ noise² in my case) and → 0 as the drive → 0, with the orientation (sign) held.
>
> I then **couple a population** of these units (symmetric/diffusive coupling through their order-parameter directions) and form a **mean field** as the population average of their order-parameter vectors. I can form it two ways:
> - **normalized** (average the *unit* vectors): an **orientation consensus** — which way the population's winding points.
> - **non-normalized** (average the *full* vectors, weighted by each unit's current magnitude): a **flux-weighted consensus** — which cancels to ~0 if the units' orientations disagree, and is dominated by the highest-current units if they agree.
> A slower collective circulation can emerge among the coupled units (a "meta-cycle").
>
> **QUESTIONS** (please give named results/theorems + citations; flag non-standard or wrong framing):
>
> **1. The two mean fields.** Is the distinction between the *normalized* (orientation) consensus and the *non-normalized* (amplitude/flux-weighted) consensus the standard **phase-order-parameter vs amplitude-order-parameter** distinction? My guess: the normalized average is the **Kuramoto order parameter** (phase synchronization, amplitude-independent) and the non-normalized is the **Stuart–Landau / complex Ginzburg–Landau mean field** (amplitude matters). Is that the right mapping? Is there a standard name for the fact that the flux-weighted mean **cancels for incoherent orientations** even when each unit is strongly driven (e.g. **amplitude death / oscillation death**, Aronson–Ermentrout–Kopell)?
>
> **2. Separating drive from structure.** In stochastic thermodynamics the steady-state entropy-production rate factorizes as ⟨σ⟩ = J·𝒜 (current × affinity). Is decomposing the circulation into an **intensive, drive-independent affinity 𝒜** (the structural/topological force) and an **extensive, drive-set current J** the standard and correct way to isolate "the drive" from "the structure"? Is the affinity's drive-independence (exact in the linear/OU regime) a known general result or a linear-regime artifact? What bounds the current at fixed affinity — is this exactly the **thermodynamic uncertainty relation**, and is the **Harada–Sasa equality** the right tool relating current, drive, and dissipation?
>
> **3. Two channels threading a hierarchy.** Going up a coarse-graining hierarchy (eliminate fast modes, keep slow), is it established that the **orientation / topological invariant is preserved (drive-independent)** while the **current magnitude renormalizes** (setting a slower collective flow rate)? I.e. the winding sign threads up invariant, the flux renormalizes by the coarse-graining timescale. Where does this two-channel behaviour live — **coarse-graining of Markov-jump currents** (Esposito and co.; affinity preserved, rate renormalized under timescale separation), persistence of **topological / Betti invariants** under reduction, and renormalization of currents/rates under elimination of fast modes?
>
> **4. Heterogeneity and relative internal scale.** With a *distribution* of internal frequencies/affinities across units: (a) how does the dispersion detune the orientation lock — is this the **Kuramoto critical coupling** K_c(frequency-spread)? (b) does it bias the flux-weighted mean toward the loudest (highest-current) units? (c) is the separation between the *fast* internal cycle and the *slow* collective mode the standard **slow–fast / averaging / Haken-slaving** setup, and does that timescale ratio set whether the collective flux is a clean slow variable?
>
> **5. The high-drive ceiling.** In the linear/OU regime the affinity is drive-independent and the drive is a clean *multiplicative* flow-rate knob **orthogonal** to the topological invariant. When does this break — i.e. when does strong drive stop being orthogonal and instead **change the invariant** (destabilize the stable focus into a limit cycle, or push the trajectory into the nonlinear region where the rotation axis distorts)? What governs the validity range of the small-noise / linear-response regime — **Freidlin–Wentzell** large deviations, the **Kramers / escape** scale, the distance to the nearest bifurcation? Is there a clean criterion for "drive too strong → the carrier of the topological bit destabilizes"?
>
> **Please give named results/theorems + citations, and correct any place where the framing is non-standard or loose.**

---

model a:
This is actually a fairly mature decomposition, but your language mixes three different notions that the literature usually keeps separate:

1. **Topology/chirality of the cycle** (orientation, homology class, winding sign).
2. **Thermodynamic force** (affinity, cycle affinity, housekeeping drive).
3. **Flux/current magnitude** (probability current, cycle current, circulation rate).

The strongest correction I'd make is:

> The sign of the affinity and the sign of the current coincide only sufficiently near a fixed network structure. They are not the same invariant. The true invariant is the oriented cycle itself (the homology class / cycle basis element). Affinity is a force defined on that cycle; current is the response.

That distinction becomes important once nonlinearities, bifurcations, or coarse-graining enter.

---

# 1. The two mean fields

Your mapping is mostly right.

## Normalized mean field

If each oscillator contributes only a direction,

[
\hat z_i = e^{i\theta_i},
]

then

[
R e^{i\Psi}
===========

\frac1N\sum_i e^{i\theta_i}
]

is exactly the standard **Kuramoto order parameter**.

Re^{i\Psi}=\frac{1}{N}\sum_{j=1}^{N}e^{i\theta_j}

This measures orientation/phase consensus independent of amplitude.

Canonical references:

* Yoshiki Kuramoto (1975, 1984)
* Steven Strogatz (2000 review)
* Ernest Barreto and others in phase reduction literature.

This is the standard "phase-only" collective variable.

---

## Flux-weighted mean field

If instead

[
Z=\frac1N\sum_i A_i e^{i\theta_i},
]

with (A_i) proportional to current magnitude or oscillation amplitude, then you have entered the territory of

* Stuart–Landau oscillators,
* complex Ginzburg–Landau equations,
* Ott–Antonsen reductions with amplitude,
* Landau mean-field theory of oscillations.

The order parameter is no longer purely orientational.

The dominant contributors are the largest-amplitude oscillators.

That is exactly the distinction between:

* phase coherence,
* amplitude-weighted coherence.

---

## Is cancellation "amplitude death"?

Not quite.

If orientations are incoherent,

[
\sum_i A_i e^{i\theta_i}\approx 0,
]

that is simply **destructive vector averaging** or **loss of phase coherence**.

Amplitude death is stronger:

[
A_i\to 0
]

for each oscillator.

References:

* Daniel Aronson
* John Ermentrout
* Nancy Kopell

So:

| phenomenon        | amplitudes                   | mean field |
| ----------------- | ---------------------------- | ---------- |
| incoherence       | finite                       | cancels    |
| amplitude death   | vanish                       | vanishes   |
| oscillation death | symmetry-broken fixed points | vanishes   |

These are distinct.

---

# 2. Separating drive from structure

This is where stochastic thermodynamics already has almost exactly your decomposition.

The central result is the cycle decomposition of nonequilibrium steady states.

References:

* Terrell Hill
* Jürgen Schnakenberg
* Massimiliano Esposito

Schnakenberg's framework writes entropy production as

[
\dot S
======

\sum_\alpha J_\alpha A_\alpha
]

where

* (A_\alpha) = cycle affinity
* (J_\alpha) = cycle current

and the decomposition is physically meaningful.

\dot S=\sum_{\alpha}J_{\alpha}A_{\alpha}

Your "structure vs drive" language maps naturally onto

| your term   | stochastic thermodynamics |
| ----------- | ------------------------- |
| orientation | cycle orientation         |
| invariant   | cycle basis element       |
| affinity    | thermodynamic force       |
| magnitude   | cycle current             |

---

## Is affinity drive-independent?

This is where I would soften your claim.

For a Markov network,

[
A=\ln\frac{\prod k_+}{\prod k_-}
]

depends on the rates.

If your "drive amplitude" rescales all rates equally,

[
k_\pm \rightarrow \lambda k_\pm,
]

then affinity remains unchanged while current scales.

That is exactly what you are observing.

But this is not a universal theorem.

If the drive changes forward/backward asymmetry,

then affinity changes too.

So:

* exact in many OU-like constructions,
* exact under common multiplicative rate scaling,
* not generally true far from equilibrium.

---

## What limits current at fixed affinity?

Several answers exist.

### Linear response

Near equilibrium:

[
J=L A
]

(Onsager).

### Far from equilibrium

Current is constrained by dissipation and fluctuations.

The major modern result is indeed the

**Thermodynamic Uncertainty Relation (TUR)**.

References:

* Andreas Barato
* Udo Seifert

The TUR bounds precision of a current by entropy production.

---

## Harada–Sasa?

Yes, but slightly differently than you frame it.

The **Harada–Sasa equality** relates

* violation of fluctuation-dissipation balance,
* energy dissipation rate.

References:

* Takahiro Harada
* Shin-ichi Sasa

It is a dissipation estimator rather than a current bound.

TUR and Harada–Sasa are complementary.

---

# 3. Coarse-graining hierarchy

This is probably the deepest part of your picture.

The literature says:

## Affinities often survive coarse-graining

Under timescale separation, eliminating fast states frequently preserves effective cycle affinities.

This appears in:

* Massimiliano Esposito
* Christian Maes
* Rao Rao

The effective network inherits cycle forces.

---

## Currents renormalize

The current scale changes because effective transition rates change.

This is essentially a dynamical renormalization.

Fast loops disappear.

Slow loops remain.

Flux gets rescaled.

That part of your intuition is standard.

---

## Topology survives better than rates

This is where your "two-channel" language is strongest.

Homological structure is much more robust than kinetic details.

The relevant mathematics comes from

* graph homology,
* persistent homology,
* Hodge decomposition of currents.

References:

* Eckmann Pierre
* Mikael Djurfeldt

Cycle spaces survive reductions far more readily than precise flux magnitudes.

That is a real asymmetry.

---

# 4. Heterogeneity and internal scale

Your mapping is basically standard.

## (a) dispersion vs locking

Yes.

Frequency spread competes with coupling.

For unimodal distributions,

[
K_c
===

\frac{2}{\pi g(0)}
]

is the classical Kuramoto threshold.

K_c=\frac{2}{\pi g(0)}

Greater dispersion ⇒ harder synchronization.

---

## (b) loudest oscillators dominate

Yes.

In amplitude-weighted means,

high-current/high-amplitude oscillators contribute disproportionately.

This is standard in Stuart–Landau populations.

---

## (c) slow collective mode

Exactly.

Your description fits

* averaging theory,
* singular perturbation theory,
* center-manifold reduction,
* Haken's slaving principle.

References:

* Hermann Haken
* Neil Fenichel

The collective mode is clean when

[
\tau_{\rm collective}
\gg
\tau_{\rm internal}.
]

---

# 5. When does orthogonality fail?

This is where your proposed "topological bit" becomes delicate.

In the linear regime,

orientation and current magnitude are approximately orthogonal coordinates.

But three mechanisms destroy that separation.

---

## A. Bifurcation

Crossing a

* Hopf bifurcation,
* saddle-node of cycles,
* homoclinic bifurcation,

changes the attractor itself.

The carrier of the circulation changes.

References:

* Yuri Kuznetsov

This is probably the cleanest failure mode.

---

## B. Noise-induced escapes

If noise reaches the Freidlin–Wentzell quasipotential barrier,

[
P \sim e^{-\Delta V/\epsilon}
]

rare transitions invalidate local linearization.

genui{"math_block_widget_always_prefetch_v2":{"content":"P\sim e^{-\Delta V/\varepsilon}"}}

References:

* Mark Freidlin
* Alexander Wentzell

---

## C. Nonlinear distortion

Far from the fixed point,

the Jacobian no longer controls rotation.

The effective circulation axis changes.

The cycle affinity itself may become state dependent.

Then the clean decomposition breaks down.

---

# Overall assessment

The most established formulation of what you are describing is not actually "drive vs topology."

The literature would phrase it as:

> **Cycle-space structure (oriented cycles) + thermodynamic affinities (forces) + cycle currents (responses).**

That triad comes from Schnakenberg network thermodynamics and stochastic thermodynamics.

Your proposed hierarchy then becomes:

1. **Cycle orientation / homology class** — most robust, often preserved under coarse-graining.
2. **Affinity** — effective nonequilibrium force associated with that cycle.
3. **Current magnitude** — kinetic quantity that renormalizes strongly and sets dissipation.

That decomposition is very close to established theory, and in my view it is a cleaner formulation than "topological invariant vs drive" because it separates the genuinely topological object (the cycle) from the thermodynamic force (affinity) that acts on it.

model b:
Your framing is highly intuitive and conceptually elegant. You are effectively bridging **stochastic thermodynamics** (cycle affinities, entropy production) with **nonlinear dynamics** (coupled oscillators, mean fields). Your physical intuition is largely correct, but there are a few places where your terminology misaligns with established literature, particularly regarding what constitutes a "drive" and the distinction between incoherence and amplitude death.

Here is the breakdown of the literature, the specific named theorems/results, and where your framing requires minor adjustments.

---

### 1. The Two Mean Fields

Your mapping of the two mean fields is spot on, but your terminology regarding the cancellation of the flux-weighted mean needs correction.

* **The Normalized Mean (Phase Consensus):** You are exactly right. This is the **Kuramoto order parameter**, defined mathematically as $R e^{i\Phi} = \frac{1}{N} \sum_{j} e^{i\theta_j}$. It characterizes purely topological phase synchronization and ignores the current/amplitude magnitude.
* **The Non-Normalized Mean (Flux-Weighted Consensus):** This maps directly to the mean field of the **Complex Ginzburg–Landau Equation (CGLE)** or coupled **Stuart–Landau oscillators**. When units have both amplitude $\rho_j$ and phase $\theta_j$, the order parameter is $Z = \frac{1}{N} \sum_{j} \rho_j e^{i\theta_j}$. This is standard in amplitude-phase models (e.g., the Matthews–Mirollo–Strogatz model of coupled limit-cycle oscillators).
* **CORRECTION (Amplitude Death vs. Incoherence):** You hypothesized that the flux-weighted mean canceling out for incoherent orientations is called "amplitude death" or "oscillation death." **This is incorrect.** * **Phase Incoherence (Desynchronization):** If the individual units are strongly driven (rotating with large $\rho_j$) but their phases $\theta_j$ are uniformly distributed, $Z \approx 0$ due to destructive interference. The units are still oscillating; the *population* is just macroscopic noise.
* **Amplitude/Oscillation Death (Aronson–Ermentrout–Kopell / Bar-Eli effect):** This is a phenomenon where the *coupling itself* pulls the individual units off their limit cycles and stabilizes a previously unstable fixed point (the origin). In amplitude death, $\rho_j \to 0$ for every unit.



### 2. Separating Drive from Structure

Your decomposition is mathematically sound, but your use of the word "drive" differs from the standard conventions of stochastic thermodynamics.

* **Cycle Affinities and Currents:** Decomposing entropy production into $\langle \sigma \rangle = \sum J_\alpha \mathcal{A}_\alpha$ is strictly codified in **Schnakenberg’s network theory** (macroscopic cycle decomposition) and **Hill’s cycle theory** of non-equilibrium steady states (NESS).
* **CORRECTION (Affinity vs. Drive):** In standard stochastic thermodynamics, the affinity $\mathcal{A}$ *is* the thermodynamic drive (the non-conservative force). For a cycle, $\mathcal{A} = \ln \prod (k^+/k^-) = W / k_B T$, where $W$ is the work done around the loop.
* If you define "drive" as the noise amplitude (temperature $T$), then increasing the drive *decreases* the affinity $\mathcal{A}$ unless the work $W$ scales proportionally with the noise.
* The fact that your affinity is strictly independent of the noise amplitude is a specific artifact of the linear (Ornstein–Uhlenbeck) regime with additive noise where the drift vector field scales perfectly with the diffusion tensor. It is not a general property of nonlinear NESS.


* **The Thermodynamic Uncertainty Relation (TUR):** You are completely right to invoke the TUR (Barato & Seifert, 2015). It dictates that the precision of the current is bounded by the dissipation: $\text{Var}(J)/\langle J \rangle^2 \ge 2 k_B / \langle \sigma \rangle$. Because $\langle \sigma \rangle = J \mathcal{A}$, the TUR explicitly bounds the extensive current variations against the intensive structural affinity.
* **Harada–Sasa Equality (2005):** This is exactly the right tool. It relates the energy dissipation in a NESS to the extent to which the system violates the **Fluctuation-Dissipation Theorem (FDT)**. It effectively maps the relationship between your "drive" (noise/fluctuations) and the resulting nonequilibrium current.

### 3. Two Channels Threading a Hierarchy

The idea that the topological invariant (orientation) threads upward while the rates (currents) renormalize under coarse-graining is a well-established phenomenological observation, heavily formalized in the last decade.

* **Coarse-Graining of Markov Networks:** Look to the work of M. Esposito (e.g., *Stochastic thermodynamics under coarse graining*, 2012) and S. Rahav & C. Jarzynski (2007). The standard result is that coarse-graining (decimating fast variables) strictly *reduces* or bounds the apparent entropy production because hidden cyclic micro-currents are integrated out.
* **Topological/Betti Invariants:** Your framing of "orientation" is formalized in **Homological cycle thermodynamics** (see Polettini, *Cycle thermodynamics of complex networks*, 2015; and Baez). The orientation of your cycle corresponds to the sign of the current along the generators of the first homology group (the Betti numbers) of the Markov graph.
* **Renormalization:** The preservation of topological invariants while rates renormalize is explored in **decimation schemes for Markov jump processes** (e.g., Altaner & Vollmer, *Fluctuation-preserving coarse graining for biochemical systems*, 2012). The winding sign survives as long as the coarse-graining doesn't lump states that break the cycle's homology.

### 4. Heterogeneity and Relative Internal Scale

* **a) Detuning via Dispersion:** Yes, this is governed by the **Kuramoto Critical Coupling** $K_c$. If the spread of internal frequencies (or cycle affinities) is given by a distribution $g(\omega)$, synchronization only occurs when the coupling $K > K_c = 2 / (\pi g(0))$.
* **b) Bias Toward Loud Units:** This is a known feature in generalized CGLE networks. In models coupling both phase and amplitude, units with a larger limit-cycle radius ($\rho$) exert a stronger pull on the mean field, effectively weighting the collective phase toward the high-flux units.
* **c) Slow-Fast Separation:** Yes, this is the standard **Haken Slaving Principle** (from synergetics) or the **Center Manifold Theorem**. In the context of oscillators, you can also look up **Averaging Theory** (Bogoliubov–Krylov–Mitropolsky), which formalizes how fast cyclic variables are averaged out to yield equations strictly governing the slow collective amplitudes and phase differences.

### 5. The High-Drive Ceiling

Your intuition here maps directly to the breakdown of linear response and noise-induced transitions.

* **Small-Noise Validations:** The regime where your "topological bit" is cleanly preserved is the **Linear Response Regime** (Kubo).
* **Freidlin–Wentzell Theory & Large Deviations:** You nailed this. Freidlin–Wentzell theory governs the large deviation principle for stochastic differential equations. It defines the characteristic timescale for a noise-driven system to escape an attractor (the **Kramers escape time**, scaling as $\tau \propto \exp(\Delta U / D)$).
* **Changing the Invariant:** When the noise (drive) is strong enough to push the system out of the basin of attraction of the stable focus, or broadens the stationary distribution so much that the "hole" in the center of the limit cycle is filled in, the system undergoes a **Noise-Induced Bifurcation** (or *Noise-Induced Topological Transition*). The foundational text here is Horsthemke & Lefever (*Noise-Induced Transitions*, 1984). The clean criterion for "drive too strong" is when the noise amplitude $D$ becomes comparable to the deterministic barrier height $\Delta U$ separating the cyclic attractor from other states (or separating the focus from the origin).

---

To ensure I point you toward the most useful mathematical techniques for your specific setup: Does your coupling function contain only diffusive (dissipative) terms, or does it include reactive (non-isochronous) cross-coupling between the phase and amplitude, such as the shear parameter in the Stuart-Landau equation?
model c:

I'll search the specific literature you reference to verify your framing and locate the precise theorems/citations.


Below is a section-by-section audit of your framing, with named theorems, correct citations, and flags where the language is non-standard or physically loose.

---

## 1. The two mean fields

**Your mapping is essentially correct, but the terminology needs tightening.**

- **Normalized consensus** = **Kuramoto order parameter**  
  \(r\,e^{i\psi}=N^{-1}\sum_j e^{i\theta_j}\). This is a pure phase order parameter; amplitude information is discarded by projection onto the unit circle. It measures *orientation* (phase) coherence and is insensitive to the magnitude of the individual limit-cycle oscillations.

- **Non-normalized consensus** = **Stuart–Landau / complex Ginzburg–Landau (CGLE) mean field**  
  \(N^{-1}\sum_j A_j\,e^{i\theta_j}\) where \(A_j\) is the local amplitude. In the CGLE literature this is the *amplitude* (or envelope) order parameter. The CGLE is the normal form of a supercritical Hopf bifurcation and describes both phase and amplitude dynamics; averaging the full complex amplitudes gives a field whose magnitude reflects both phase alignment and amplitude growth.

**Flag (non-standard framing):**  
The cancellation of the flux-weighted mean for incoherent orientations is *not* amplitude death / oscillation death (AD/OD). AD/OD refers to coupling-*induced* stabilization of a fixed point that kills the limit cycle (Aronson–Ermentrout–Kopell, *Physica D* 41, 403 (1990); Ermentrout–Kopell, *SIAM J. Appl. Math.* 50, 125 (1990)). What you describe—vectors adding to zero because phases are uniformly distributed—is simply the geometric cancellation of a *vector mean* when the orientational symmetry is unbroken. It occurs even for uncoupled units. AD/OD is a dynamical bifurcation phenomenon, not a static averaging artifact. Do not conflate the two.

A standard name for the amplitude-weighted cancellation in the presence of strong local drive is simply **destructive interference of the order-parameter field**; in laser/CGLE language it is the regime where the macroscopic polarization vanishes while local fields remain finite.

---

## 2. Separating drive from structure

**The factorization \(\langle\sigma\rangle = J\cdot\mathcal{A}\) is standard, but your "drive-independence" claim is regime-dependent and needs qualification.**

- **Named result:** In stochastic thermodynamics the steady-state entropy-production rate decomposes over a fundamental set of independent cycles \(\mathcal{C}\) as  
  \(\sigma = \sum_{\mathcal{C}} J_{\mathcal{C}}\,\mathcal{A}_{\mathcal{C}}\),  
  where \(J_{\mathcal{C}}\) is the stationary cycle current and \(\mathcal{A}_{\mathcal{C}}=\ln\prod_{(i,j)\in\mathcal{C}}(w_{ij}/w_{ji})\) is the cycle affinity (Schnakenberg, *Rev. Mod. Phys.* 1976; Hill, *Free Energy Transduction* 1989; Seifert, *Rep. Prog. Phys.* 2012).

- **Drive-independence of affinity:** This is *not* a universal theorem; it holds in your setup because the "drive" you dial is a *multiplicative prefactor* (noise strength, temperature, or a common scaling of kinetic rates) that affects forward and backward rates symmetrically. Since \(\mathcal{A}\) is a log-ratio of rate-products, any common prefactor cancels. If, however, the drive is a thermodynamic force such as a chemical-potential difference \(\Delta\mu\) or an external field \(F\), then \(\mathcal{A}\propto \Delta\mu/k_BT\) or \(\mathcal{A}\propto F\), and the affinity *does* depend on the drive amplitude. Your statement is correct only when the drive is orthogonal to the force landscape (e.g. thermal noise at fixed \(\Delta\mu\)).

- **Bounding current at fixed affinity:** Yes, the **Thermodynamic Uncertainty Relation (TUR)** is the right tool. Barato & Seifert proved the generic bound  
  \(\sigma \ge J^2/D_J\) (equivalently \(\text{Var}(J)\, \sigma \ge 2J^2\) in the long-time limit),  
  which at fixed affinity \(\mathcal{A}\) bounds the current \(J\) through the entropy production \(\sigma\). Tightening for specific topologies was done by Polettini, Falasco & Esposito (*Phys. Rev. E* 106, 064121 (2022)) and Pietzonka, Barato & Seifert (*Phys. Rev. E* 93, 052145 (2016)).

- **Harada–Sasa equality:** This is the correct relation connecting dissipation to the violation of the fluctuation-dissipation theorem (FDT). For Langevin dynamics,  
  \(\int_{-\infty}^{\infty}[\tilde{C}_x(\omega)-2T\tilde{R}'_x(\omega)]\frac{d\omega}{2\pi} = \dot{q}/\gamma\). It gives the *total* dissipation associated with an observed coordinate. For Markov jump processes the equality breaks down if forward/backward rates respond asymmetrically to perturbation; a renormalized version exists when the entropy production per jump is small (Wang, *Phys. Rev. E* 97, 052125 (2018)).

**Flag (loose framing):**  
Do not say the affinity is "topological." It is a *discrete* (structural) invariant of the network graph, but it is not a topological invariant in the sense of homotopy/Betti. It is a thermodynamic force assigned to a cycle.

---

## 3. Two channels threading a hierarchy

**Your intuition is correct and matches several established results, but the literature is fragmented.**

- **Affinity preservation under coarse-graining:**  
  Polettini & Esposito (*J. Stat. Phys.* 2019) developed an "effective fluctuation and response theory" showing that when an observer only measures a subset of currents, the hidden cycles can be integrated out leaving **effective affinities** that are operationally defined by tuning to stalling. The structural/topological force is preserved (or re-summed into effective affinities) while the effective rates are renormalized. Rao & Esposito (*New J. Phys.* 2021) and related work by Bulnes show that coarse-graining in cycle space (or "milestoning" with timescale separation) preserves the affinity while modifying the rate constants.

- **Topological invariants under reduction:**  
  Haken's **slaving principle** states that fast-relaxing (stable) modes are enslaved by slow order-parameter modes; the slow manifold inherits the topological character of the bifurcation. In your language, the winding sign (chirality) is the order-parameter symmetry and is preserved under adiabatic elimination of fast modes.

- **Renormalization of currents/rates:**  
  When fast modes are eliminated (e.g., via center-manifold or averaging methods), the reduced dynamics lives on a slower timescale. The current on the slow manifold is renormalized by factors of the fast-mode relaxation rate. This is the standard **adiabatic elimination** or **projected dynamics** result (Kuramoto's reduction via Floquet eigenvectors, Haken's averaging).

- **Betti invariants under RG:**  
  In a different but related literature, simplex renormalization group flows can preserve Betti numbers (counts of \(m\)-dimensional holes) when the system is near a scale-invariant fixed point. This is not yet standard in stochastic thermodynamics, but it supports your "two-channel" picture: homology classes persist, metric quantities (rates, currents) flow.

**Flag (non-standard):**  
"Topological invariant is preserved" is accurate for the *chirality* (sign of winding), but be careful: if the coarse-graining eliminates the cycle entirely (e.g. merging all three states of your 3-state Markov loop into one macrostate), the homology class is destroyed, not preserved. The affinity is preserved only when the coarse-graining respects the cycle topology (e.g. milestoning that keeps the loop intact).

---

## 4. Heterogeneity and relative internal scale

**(a) Dispersion detuning orientation lock:**  
Yes. For a unimodal symmetric frequency distribution \(g(\omega)\), the **Kuramoto critical coupling** is  
\(K_c = \frac{2}{\pi g(0)}\)  
(Kuramoto 1984; Strogatz 2000; Acebrón et al., *Rev. Mod. Phys.* 77, 137 (2005)). For bounded distributions, Ermentrout gave the tight bound  
\(\omega_{\max}/K_c = \max_{p\ge 1}\{p^{-2}\int_{-1}^{1}\sqrt{p^2-\omega^2}\,g(\omega)\,d\omega\}\).

**(b) Bias of flux-weighted mean toward highest-current units:**  
This is not a named theorem in the oscillator literature, but it is a generic property of any weighted average: the mean is pulled toward units with larger weights (current magnitudes). In the CGLE/Kuramoto context, this is related to the fact that the **amplitude order parameter** is dominated by synchronized clusters with large amplitude. There is no standard "loudest-unit theorem," but the effect is well-known in mean-field CGLE analyses.

**(c) Slow-fast / Haken-slaving:**  
Yes. The separation between fast internal cycling and slow collective mode is the standard **slow–fast** or **adiabatic elimination** setup. Haken's slaving principle explicitly states that fast variables are prescribed by slow order parameters. The ratio of timescales \(\tau_{\text{fast}}/\tau_{\text{coupling}}\) determines whether the collective flux is a clean slow variable. If the ratio is \(\ll 1\), the amplitudes adiabatically follow the phase dynamics and the collective current is a valid slow observable. If the ratio is \(\mathcal{O}(1)\), the slaving breaks down and you need full phase-amplitude reduction (e.g. Kuramoto's reductive perturbation or isostable reduction).

---

## 5. The high-drive ceiling

**Your geometric intuition is right, but the "orthogonality" framing is non-standard.**

- **Validity of linear-response / small-noise regime:**  
  The **Freidlin–Wentzell (FW) large-deviation theory** gives the quasipotential \(V(x)\) governing the probability of rare trajectories. In the weak-noise limit, the stationary distribution is \(\rho(x)\sim e^{-V(x)/\varepsilon}\). Santolin, Freitas, Esposito & Falasco (*Phys. Rev. E* 111, 024106 (2025)) proved a series expansion of the quasipotential around the detailed-balance (equilibrium) solution and identified the conditions for the **linear-response regime** to hold even far from equilibrium: the nonequilibrium drive must be small enough that the first-order correction to the quasipotential suffices.

- **Escape-rate / Kramers criterion:**  
  The **Kramers escape rate** (or Arrhenius factor) sets the timescale for noise-induced transitions out of a metastable state. When the drive is strong enough to significantly alter the quasipotential barrier height or to change the fixed-point structure, the small-noise expansion fails.

- **Bifurcation criterion:**  
  The cleanest criterion for "drive too strong" is **structural instability**: when the nonequilibrium drive parameter crosses a bifurcation value (Hopf, SNIC, saddle-node), the topological carrier of the circulation changes. Before the bifurcation, the rotation axis is a stable focus; after, it may become a stable node or a limit cycle may be born/destroyed. The distance to the nearest bifurcation in parameter space sets the radius of validity of the linear regime.

**Flag (loose framing):**  
You describe the drive as "orthogonal" to the topological invariant. This is a useful heuristic but not a formal theorem. In dynamical-systems terms, the drive parameter and the bifurcation parameter are not necessarily orthogonal vectors in parameter space; rather, the topological invariant (the chirality / winding number) is protected by a **structural stability** region bounded by bifurcation surfaces. The drive stops being a "clean multiplicative knob" when it pushes the system across such a surface.

**Named results to cite for the ceiling:**
- **Freidlin–Wentzell quasipotential** and **noise-induced exit** (FW 1984; Varadhan's Lemma).
- **Santolin et al. 2025**: bounds on escape rates from dissipative fixed points in terms of entropy production of relax/escape trajectories.
- **Harada–Sasa / TUR**: give bounds on fluctuations and dissipation within the regime where the steady-state topology is unchanged, but they do not predict the bifurcation point. For that, you need normal-form / bifurcation theory (Guckenheimer & Holmes).

---

## Summary of corrections

| Your framing | Verdict | Correction |
|---|---|---|
| Normalized = Kuramoto, non-normalized = Stuart-Landau/CGLE | **Correct** | Tighten: CGLE is the *amplitude* order parameter. |
| Flux-weighted cancellation = amplitude death | **Loose / Wrong** | Vector cancellation ≠ AD/OD. AD is a coupling-induced bifurcation. |
| Affinity is drive-independent | **Conditionally correct** | True only if "drive" is a symmetric prefactor (noise, temp). False if drive is \(\Delta\mu\) or field. |
| Affinity is "topological" | **Loose** | It is structural (graph-cycle) but not a Betti/homotopy invariant. |
| TUR bounds current at fixed affinity | **Correct** | Use Barato–Seifert 2015, Gingrich et al. 2016, Polettini–Falasco–Esposito 2022. |
| Harada–Sasa relates current, drive, dissipation | **Correct for Langevin** | For Markov jumps, needs small-entropy-per-jump or symmetric perturbation. |
| Orientation preserved, current renormalized under CG | **Correct** | Cite Polettini–Esposito effective affinities and Haken slaving. |
| Kuramoto \(K_c\) for frequency dispersion | **Correct** | Cite \(K_c=2/\pi g(0)\) and Ermentrout's bounds. |
| Slow-fast = Haken slaving | **Correct** | Timescale ratio must be \(\ll 1\) for clean slaving. |
| Drive orthogonal to topological bit | **Heuristic only** | Formal criterion is distance to bifurcation / structural stability boundary. |

If you want, I can expand any of these into explicit equations or map them onto your 3-state Markov / Stuart-Landau concrete model.

---

## SYNTHESIS — what the three models settle, and what was applied (2026-05-30)

**Headline: MPA already owns most of this.** The affinity/current split, TUR, Harada–Sasa, Kuramoto,
slaving are all already in `mpa_prior_art.md` (`cycle-affinity`, `tur`, `harada-sasa`, `kuramoto`,
`slaving`). The research *confirms* those and delivers four corrections + one clean new home.

**CONSENSUS (all three):**
- **Q1.** normalized average = **Kuramoto order parameter** (phase, amplitude-blind); non-normalized =
  **Stuart–Landau / CGLE amplitude order parameter** $N^{-1}\sum_j A_j e^{i\theta_j}$ (Matthews–Mirollo–
  Strogatz). Mapping correct.
- **Q2.** $\langle\sigma\rangle=\sum_\alpha J_\alpha\mathcal{A}_\alpha$ (Schnakenberg/Hill/Seifert) is the
  standard, correct drive-vs-structure decomposition. TUR (Barato–Seifert) is the right current bound at
  fixed affinity; Harada–Sasa the right dissipation/FDR-violation estimator (complementary, not a bound).
- **Q3.** CONFIRMED and this is the clean new home: affinity preserved under coarse-graining, currents
  renormalize, topology survives better than rates (Esposito 2012; **Polettini–Esposito effective
  affinities**, JSP 2019; Rao–Esposito NJP 2021; **Altaner–Vollmer** fluctuation-preserving decimation
  2012; Hodge decomposition of currents).
- **Q4.** dispersion→**Kuramoto $K_c=2/\pi g(0)$** (Ermentrout tight bound); loudest units dominate the
  amplitude mean (generic weighted-average, no named theorem); slow–fast = **Haken slaving / averaging
  (Bogoliubov–Krylov–Mitropolsky)**, clean only for $\tau_{\rm fast}/\tau_{\rm coupling}\ll1$.
- **Q5.** the clean ceiling criterion is **distance to the nearest bifurcation / structural stability**
  (Hopf/SNIC/saddle-node; Kuznetsov, Guckenheimer–Holmes), with **Freidlin–Wentzell** quasipotential /
  **Kramers** escape for the noise-induced route (Horsthemke–Lefever noise-induced transitions; Santolin
  et al. PRE 111, 024106 (2025) for the linear-response-far-from-equilibrium validity window).

**FOUR CORRECTIONS to my framing (all flagged by ≥2 models):**
1. **Flux cancellation ≠ amplitude death.** Incoherent vector cancellation ($\sum A_j e^{i\theta_j}\approx0$
   with $A_j$ finite) is **destructive interference of the order-parameter field / loss of phase
   coherence**, and happens even uncoupled. **Amplitude/oscillation death** (Aronson–Ermentrout–Kopell,
   Bar-Eli) is a *coupling-induced bifurcation* driving each $A_j\to0$. Distinct — do not conflate. (I
   conflated them in the chat framing; corrected.)
2. **Affinity drive-independence is regime-specific, not a theorem.** It holds because *our* drive (noise
   amplitude σ) is a **symmetric multiplicative prefactor** that cancels in the log-ratio $\ln\prod k_+/\prod
   k_-$. If the drive is a thermodynamic *force* ($\Delta\mu$, external field), $\mathcal{A}\propto\Delta\mu/k_BT$
   **does** depend on the drive. So "the drive lives only in $J$" is the additive-noise/OU case. → scope on #2.
3. **Affinity is NOT "topological."** It is a *structural* (graph-cycle) quantity / thermodynamic **force**,
   not a Betti/homotopy invariant. The genuinely topological object is the **oriented cycle itself (the
   homology class / cycle-space basis element)**. Cleaner triad than my two-way split:
   **(i) oriented cycle / homology class** (topological, most robust under CG) → **(ii) affinity** (force on
   it) → **(iii) current** (kinetic response, renormalizes). sign($\mathcal{A}$)=sign($J$)=orientation
   coincide only near a fixed structure (model a). → engine flag below.
4. **"Drive orthogonal to the bit" is a heuristic, not a theorem.** The bit is protected by a
   **structural-stability region bounded by bifurcation surfaces**; the drive stops being a clean
   multiplicative knob when it crosses one (or when noise $D\sim$ barrier $\Delta U$). → answers my open
   Q5; engine flag below.

**APPLIED (within authority — tracking/borrowed-results currency; uncommitted, held mid-thread):**
- **prior-art:** landed the owed `esposito-coarse-graining` key (Esposito 2012 / Polettini–Esposito /
  Rao–Esposito / Altaner–Vollmer) — the establishment home for `scale-covariant-circulation` (#3), the way
  the ladder research landed `fenichel-nhim`.
- **frontier `battery:scale-covariant-circulation`:** cited the established home; noted the literature's
  "coarse-graining must respect the cycle homology" = our pre-classified **B-fail** (homology-breaking lump
  = rewiring) — independent confirmation of the kill-classification.
- **frontier `battery:dimensionless-self-probe`:** added the Q2 scope — the noise-independence of the
  affinity is the *symmetric-multiplicative-drive* (additive-noise/OU) case, NOT general drive-independence.

**FLAGGED FOR REVIEW (engine — not edited; weighty, Ron's call):**
- **Three-way vocabulary vs §TWO BITS.** MPA's two bits map cleanly (amplitude bit = current $J$; sign bit =
  **oriented homology class**, which IS topological — correct). But the engine reads the bit via
  "sign($\mathcal{A}$)" and folds the **affinity (a force, drive-dependent in general)** into "the sign bit /
  self-probe ruler." Cleaner: name the bit the *cycle orientation* (topological) and keep the *affinity*
  explicitly as the (conditionally-drive-independent) force, distinct from both orientation and current. No
  falsifier fires; it's a terminological sharpening that interacts with correction #2's scope.
- **High-drive ceiling = loss of structural stability.** Candidate import `freidlin-wentzell` (+ Kramers,
  Horsthemke–Lefever, Santolin 2025) as the home for the engine's high-energy/Wall edge: the topological bit
  is drive-independent only inside the structural-stability region; strong drive ends it at a bifurcation
  surface or when $D\sim\Delta U$. Bears on the Wall reading; hold until it serves a specific claim.
- **Candidate import (held, below entry bar):** the Stuart–Landau/CGLE **amplitude order parameter** as the
  distinct partner to `kuramoto` (the normalized/non-normalized = phase/amplitude mean-field split) — land
  it when the self-field normalized-vs-non-normalized distinction becomes load-bearing in a falsifier.

## FOLLOW-UP — the shear prediction was tested and REACHED CLOSURE-LOSS (2026-05-30)

The models' parting question (does the coupling carry shear/non-isochronicity?) was the lead. Built
`mpa-conform/scripts/clv_tower_shear.py` (fig `clv_tower_shear.png`): added shear $c$ + reactive coupling
$b$ to the coupled-SL chain and swept across the **Benjamin–Feir–Newell** threshold ($1{+}bc<0$), running
the CLV $\theta_{\min}$ diagnostic. Jacobian finite-diff-verified ($10^{-6}$) first (the CLV is only as
good as the Jacobian — fake-NaN guard). **Result:** on an $N{=}16$ CGLE ring the synchronized plateau loses
normal hyperbolicity AS $1{+}bc$ crosses 0 — $\theta_{\min}$ collapses $54°\to0.02°$ **and** $\lambda_{\max}$
turns positive ($\to+0.34$, $n_{\rm pos}{=}6$), tracking the BF threshold. So the research's non-delay shear
route **reached the closure-loss side of `battery:wall-ladder`** (deferred by `clv_tower`), giving the
discriminator both faces (plateau + closure-loss). The faithful $N{=}3$ phi-cascade *approaches* the
boundary ($\theta_{\min}\,45°\to\sim2°$) but does NOT chaos ($\lambda_{\max}{\approx}0$) — a clean instance
of *loss-of-NHIM ≠ forced chaos* (the corrected `Wall` claim). Landed prior-art `benjamin-feir`; updated
frontier `battery:wall-ladder` + `wall-as-type-boundary`. Scope: BF is a *generic* loss-of-NHIM route, not
the canonical §14 delay-Hopf (still deferred), and the decisive collapse is on the ring, not yet the
minimal cascade.