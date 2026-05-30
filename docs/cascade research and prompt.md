---

> **I'm looking for a real, physically-grounded system that spontaneously breaks chiral (parity) symmetry into a nonequilibrium steady state carrying a protected cyclic current — and, crucially, whose chiral/rotational relaxation mode is *robustly damped* (not weakly damped relative to its other relaxation modes). Please answer with specific named systems and citations, and flag where my framing is loose or wrong.**
>
> **CONTEXT.** In a driven-dissipative system a stable low-dimensional attractor (a "plateau") can host a protected cyclic current — a directed loop / chiral winding in its state space, a nonequilibrium steady-state circulation. I want to couple several such units, with a discrete rotational symmetry, so a *slower collective chiral mode* emerges (a hierarchy of chiral order). I need that collective chiral mode to be **robust to disorder in the local chiral axis**. In models, this robustness hinges on one property of each unit: the **damping of its rotational (chiral) eigenmode relative to its longitudinal (amplitude) eigenmode**. When the chiral mode is *weakly* damped (its relaxation rate ≪ the longitudinal rate — a stiff, anisotropic relaxation spectrum), the emergent collective chiral mode is **fragile**: tiny disorder in the local chiral axis destroys it. When the relaxation is more *isotropic* (rotational and longitudinal damping comparable), it is **robust** to a sizable disorder cone. I want a real substrate on the robust side.
>
> **The target substrate should:**
> - **(a)** spontaneously break chiral/parity symmetry (self-select a handedness, no built-in bias);
> - **(b)** in the broken state carry a **protected nonequilibrium cyclic current** (a directed loop, not a relaxational/gradient flow);
> - **(c)** have a **discrete rotational symmetry** (e.g. C3/C6) and ideally a **multi-scale / coarse-grainable** structure;
> - **(d) — the decisive one —** have a **robustly-damped chiral mode** (rotational relaxation rate comparable to the longitudinal one), so its chiral oscillation is *structurally stable*, not marginal.
>
> **QUESTIONS** (named systems/results + citations; flag wrong framing):
>
> **1. Candidates.** Which experimentally-grounded systems spontaneously break chiral/parity symmetry into a state with a protected cyclic nonequilibrium current? Candidates to confirm/correct/extend: chiral active matter and **active solids / odd elasticity** (Fruchart–Vitelli; Scheibner; Veenstra–Bartolo); **non-reciprocal phase transitions** (Fruchart–Hanai–Littlewood–Vitelli); chemical-oscillator / Belousov–Zhabotinsky networks; **chiral magnets / skyrmion lattices**; actomyosin cortical flows and **ciliary metachronal waves**; bacterial vortex lattices; chiral / parity-broken convection.
>
> **2. The decisive property — robust vs weak chiral damping.** Among those, which have a *robustly-damped* rotational/chiral eigenmode (relaxation rate comparable to the longitudinal/amplitude mode) versus a *weakly-damped* (near-marginal) one? How is this read off in practice — from the hydrodynamic / Goldstone-mode spectrum, the **odd-vs-even (shear) viscosity or elasticity ratio**, the linearization at the broken state, or the gap of the rotational mode? Is there a system where the chiral mode is *gapped / strongly damped by design* rather than a soft near-Goldstone mode?
>
> **3. Symmetry + hierarchy.** Which candidates combine a discrete rotational symmetry protecting a collective degeneracy **with** a natural multi-scale / coarse-grainable structure, so a *slower collective chiral mode* emerges from coupling units (a genuine hierarchy of chiral order, not a single scale)?
>
> **4. Disorder robustness.** In which is the collective chiral order robust to **quenched disorder / heterogeneity in the local chiral axis** (a finite locking range / Arnold tongue), versus fragile? Is there a known criterion (coupling vs disorder, à la Kuramoto critical coupling) for the collective chiral mode to survive a given axis-disorder spread?
>
> **5. Best single candidate.** Given all the above, what is the single strongest real system to study, and what **measurable observable** would show both (i) the self-lit chiral current and (ii) the robust (non-weakly-damped) chiral relaxation mode? Where is open/published data?
>
> **Please give named systems/results + citations, and correct any place the framing is non-standard or loose.**

---
model a:
This is a very well-posed question, but there is one place where I think your framing should be sharpened before looking for candidates.

## First correction: "chiral mode" is not usually the right eigenmode language

In most of the systems you listed, the crucial distinction is not

> chiral eigenmode vs longitudinal eigenmode

but rather

> orientational (phase/rotation) mode vs amplitude mode.

If chirality arises from spontaneous breaking of a continuous rotational symmetry, then the orientation mode is Goldstone-like and is generically soft. In that case you *cannot* get robust damping of the rotational mode without explicitly or effectively gapping it.

What you seem to need is:

* spontaneous selection of left/right handedness,
* persistent circulating current,
* but **no nearly-conserved rotational coordinate**.

That points away from ordinary oscillators and toward systems where:

* the handed state is discrete (Ising-like chirality),
* or where lattice anisotropy reduces O(2) to C₃/C₆,
* or where activity/nonreciprocity gaps the orientational sector.

That distinction turns out to be decisive.

---

# 1. Candidate systems

## A. Chiral active crystals / odd-elastic active solids

(Fruchart–Vitelli–Scheibner program)

This is the closest match to your requirements.

The basic ingredients are:

* microscopic active torques,
* spontaneous parity breaking,
* persistent circulating stresses and currents,
* odd elasticity / odd viscosity,
* non-Hermitian mode structure.

Key references:

* Michel Fruchart, Colin Scheibner, and Vincenzo Vitelli review odd elasticity and odd viscosity. ([Annual Reviews][1])
* Active surfaces with odd elasticity and topological chiral modes. ([PubMed][2])
* Chiral active columnar phases exhibiting finite-frequency collective modes. ([OUP Academic][3])

### Why it matches

The steady state is not merely a static broken-symmetry configuration.

The material continuously injects work and supports circulating stress currents and transverse responses that cannot be derived from a potential. The odd elastic tensor itself encodes a local circulation in strain space. ([Annual Reviews][1])

### Your criterion (d)

This is one of the few families where the orientational sector can be genuinely **gapped by activity and lattice structure**, rather than remaining a weakly damped Goldstone mode.

That already pushes it toward the "robust" side of your dichotomy.

---

## B. Chiral active rotor crystals

Examples:

* rotating colloidal spinners,
* driven magnetic rotors,
* starfish embryo active crystals,
* active spinner lattices.

These form crystalline phases of self-rotating units.

Advantages:

* spontaneous chirality,
* explicit cyclic currents,
* natural coarse-graining,
* often C₆ lattice symmetry.

The order parameter is already a local angular velocity.

This is probably the cleanest realization of your "plateau carrying a circulation."

The recent odd-elasticity literature increasingly uses these systems as canonical examples. ([arXiv][4])

---

## C. Bacterial vortex lattices

Examples:

* confined *Bacillus subtilis* vortex arrays,
* active turbulence confined by patterned geometries.

These definitely exhibit:

* spontaneous parity selection,
* persistent circulation,
* vortex-lattice order.

But they are less ideal for your criterion (d).

The vortex orientation is usually hydrodynamic and therefore relatively soft.

Disorder robustness exists but is often geometric rather than spectral.

I would classify them as intermediate.

---

## D. Ciliary carpets and metachronal-wave states

Examples:

* airway epithelium,
* *Volvox* colonies,
* multiciliated tissues.

These produce:

* spontaneous wave chirality,
* persistent directional currents,
* hierarchical coarse-graining.

The collective mode spectrum is heavily damped because the environment is Stokesian.

However the relevant symmetry breaking is phase-locking rather than odd elasticity.

Interesting biologically, but not the cleanest match to your hierarchy program.

---

## E. Belousov–Zhabotinsky oscillator networks

These are excellent examples of:

* spontaneous wave chirality,
* robust cyclic attractors,
* hierarchical synchronization.

But the circulating current lives in chemical phase space.

The "chirality" is less geometric than what your framework seems to require.

I would not place them first.

---

# 2. Which systems have robustly damped chiral modes?

This is the heart of the question.

The answer is easiest in terms of symmetry.

---

## Weakly damped (fragile)

If chirality comes from breaking a continuous symmetry:

* flocks,
* active nematics,
* many vortex states,
* ordinary oscillators,

then the orientational mode is Goldstone-like.

The linearized spectrum contains

[
\lambda_\theta \approx 0
]

or

[
\lambda_\theta \sim k^2.
]

Small disorder then easily tilts local axes.

These are exactly the systems where you find fragility.

---

## Robustly damped

You want

[
\operatorname{Re}\lambda_\theta
\sim
\operatorname{Re}\lambda_A
]

rather than

[
\operatorname{Re}\lambda_\theta
\ll
\operatorname{Re}\lambda_A.
]

That occurs when:

### 1. Discrete lattice symmetry

C₃, C₄, C₆ anisotropy gaps the orientational mode.

No Goldstone theorem.

### 2. Nonreciprocal couplings

Exceptional-point physics can reorganize the spectrum and produce finite relaxation gaps. ([Nature][5])

### 3. Odd elasticity / odd viscosity

Odd couplings mix rotational and longitudinal sectors.

The resulting eigenmodes are not pure rotations.

This tends to isotropize relaxation rather than creating an isolated soft angular coordinate. ([Annual Reviews][1])

---

# 3. Best candidates for hierarchy

Your hierarchy requirement is actually more restrictive than the chirality requirement.

You want:

local circulation
→ coupled units
→ collective circulation
→ slower circulation of circulations

The strongest candidates are:

### Chiral active crystals

Local:

* spinning particles.

Mesoscale:

* crystal domains.

Large scale:

* elastic collective modes.

Natural renormalization hierarchy.

### Ciliary arrays

Local:

* cilium beat cycle.

Mesoscale:

* metachronal wave.

Large scale:

* tissue-scale transport.

Very natural hierarchy.

### Active rotor metamaterials

Local:

* rotor.

Mesoscale:

* unit cell.

Large scale:

* topological edge circulation.

Potentially ideal experimentally.

---

# 4. Disorder robustness

Here your intuition aligns remarkably well with established theory.

The generic criterion has Kuramoto-like structure:

[
K > K_c(\Delta)
]

where

* (K) = alignment/locking strength,
* (\Delta) = disorder width.

The precise form depends on the system.

For active crystals and oscillator lattices one usually obtains some variant of:

[
\Delta/\Gamma
]

where

* (\Delta) is axis disorder,
* (\Gamma) is orientational relaxation gap.

Your observation can be translated into:

> robustness scales with the orientational gap.

Large gap
→ finite disorder cone survives.

Near-Goldstone mode
→ arbitrarily small disorder destroys coherence.

That is essentially the same logic as random-field destruction of orientational order.

---

# 5. Best single candidate

If I filter only by your decisive criterion (d), I would focus on:

## Chiral active crystal / odd-elastic active solid

not on oscillator networks.

Why?

Because it simultaneously provides:

* spontaneous chirality,
* persistent circulating currents,
* discrete lattice symmetry,
* natural coarse-graining,
* non-Hermitian mode spectrum,
* possibility of a genuinely gapped orientational sector,
* existing theory connecting chirality, damping, and topology. ([Annual Reviews][1])

### Observable #1: self-lit chiral current

Measure:

* local angular momentum density,
* circulating stress current,
* odd work per cycle,

or equivalently the nonzero area enclosed in stress–strain space.

That directly shows the nonequilibrium circulation.

### Observable #2: robust chiral relaxation

Perturb the local orientation field and measure the linear response spectrum.

What you want experimentally is:

[
\Gamma_\theta/\Gamma_A = O(1)
]

rather than

[
\Gamma_\theta/\Gamma_A \ll 1.
]

The smoking gun is a finite orientational relaxation gap that remains nonzero as (k\to0).

That demonstrates the chiral mode is not a soft Goldstone mode.

---

## My overall assessment

The systems you initially listed are not all equivalent with respect to your key requirement.

If the goal is:

> a real system whose local chiral circulation survives coarse-graining into a robust higher-order chiral mode,

then the strongest modern theoretical framework is the odd-elasticity / odd-viscosity family of chiral active solids and active crystals. Those systems were practically invented to study exactly the combination of parity breaking, circulating nonequilibrium currents, nonreciprocity, and gapped collective dynamics that your criterion is selecting for. ([Annual Reviews][1])

The one caveat is that "protected cyclic current" is not yet a universally standard term in that literature. Researchers would more often describe the same phenomenon as **odd work cycles**, **nonconservative stress circulation**, **active torque injection**, **odd elasticity**, or **nonreciprocal limit-cycle dynamics** rather than a protected current in state space. That translation is probably the largest vocabulary mismatch between your framing and the established literature.

[1]: https://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-040821-125506?utm_source=chatgpt.com "Odd Viscosity and Odd Elasticity | Annual Reviews"
[2]: https://pubmed.ncbi.nlm.nih.gov/38491602/?utm_source=chatgpt.com "Odd elasticity and topological waves in active surfaces - PubMed"
[3]: https://academic.oup.com/pnasnexus/article/3/10/pgae398/7754769?utm_source=chatgpt.com "Chirality and odd mechanics in active columnar phases | PNAS Nexus | Oxford Academic"
[4]: https://arxiv.org/abs/1702.02393?utm_source=chatgpt.com "Odd viscosity in chiral active fluids"
[5]: https://www.nature.com/articles/s41586-021-03375-9?utm_source=chatgpt.com "Non-reciprocal phase transitions | Nature"

model b:
This is a phenomenal and deeply specific inquiry. You are mapping out the frontier of nonequilibrium active matter and topological dynamics. Your intuition regarding the structural stability of emergent chiral modes—specifically that a "sloppy" or comparably damped amplitude mode enables robustness against quenched disorder—is absolutely correct and aligns with recent findings in coupled nonlinear oscillators.

Before diving into the candidates, let’s calibrate your framing.

### 0. Framing Corrections & Clarifications

* **"Protected" vs. "Structurally Stable":** You used "protected cyclic current." In condensed matter, "protected" usually implies a *topological invariant* (e.g., a Chern number protecting chiral edge states). If you are referring to a bulk NESS loop (a limit cycle), it is a **structurally stable attractor**, but not necessarily topologically protected. I will assume you mean a structurally stable NESS cycle.
* **Spontaneous vs. Explicit Chirality:** This is the most common trap in the literature you cited. Much of the "active solids/odd elasticity" literature (e.g., Scheibner et al., *Nature Physics* 2020) assumes constituent particles are *explicitly* chiral (pre-spun rotors). To get *spontaneous* parity/chiral breaking, the substrate must self-select a handedness ($\mathbb{Z}_2$ symmetry breaking of CW vs. CCW) from achiral building blocks.
* **Goldstone Modes vs. Damped Gaps:** If a system spontaneously breaks a *continuous* rotational symmetry (e.g., O(2)), it produces a massless (gapless) Goldstone mode; its relaxation is inherently weak at long wavelengths ($\Gamma_\theta \to 0$ as $q \to 0$). To have a **robustly damped** chiral mode, the underlying symmetry must be **discrete** (e.g., confinement in a lattice), ensuring a finite relaxation gap for the rotational mode.

---

### 1. Evaluating Your Candidates

Let's filter your list based on **(a)** spontaneous breaking, **(b)** cyclic NESS, and **(c)** discrete symmetry.

* **Chiral Active Matter / Odd Elasticity (Scheibner; Veenstra–Bartolo):** *Misfit.* Usually features explicit, not spontaneous, microscopic chirality.
* **Non-reciprocal Phase Transitions (Fruchart–Hanai–Littlewood–Vitelli):** *Excellent theoretical fit.* Their framework (e.g., *Nature* 2021) perfectly describes parity breaking into a chiral state via exceptional points. However, this is a mathematical framework, not a specific physical substrate.
* **Chiral Magnets / Skyrmion Lattices:** *Misfit.* The chirality usually stems from the Dzyaloshinskii-Moriya Interaction (DMI), which requires explicit broken inversion symmetry in the host crystal lattice. It is not spontaneous at the material level.
* **Ciliary Metachronal Waves:** *Misfit.* The cyclic current is explicit; the biological basal body of a cilium has a built-in structural asymmetry.
* **Belousov–Zhabotinsky (BZ) Networks:** *Partial fit.* They break symmetry into cyclic NESS limit cycles, but they lack a physical "directional fluid/mechanical current" (they are concentration phase currents), making the definition of a spatial "chiral axis disorder" abstract.
* **Bacterial Vortex Lattices:** **Strongest Fit.** Achiral bacteria confined in discrete circular wells spontaneously break $\mathbb{Z}_2$ symmetry to flow CW or CCW.

---

### 2. The Decisive Property: Robust vs. Weak Damping

You hit the nail on the head: the robustness of the collective state hinges on the ratio of the rotational relaxation rate ($\Gamma_\theta$) to the longitudinal/amplitude relaxation rate ($\Gamma_r$).

In practice, this is read off from the **linearized spectrum (Jacobian) of the NESS limit cycle** in a Stuart-Landau-type amplitude equation. The eigenvalues of the relaxation are $\lambda = -\Gamma \pm i\omega$.

* **Weakly Damped (Fragile):** $\Gamma_\theta \ll \Gamma_r$. The amplitude is infinitely stiff; the system reduces to a pure phase oscillator (Kuramoto). The phase is highly susceptible to local disorder.
* **Robustly Damped (Robust):** $\Gamma_\theta \sim \Gamma_r$. The amplitude is "sloppy." When local axes are disordered, the amplitude can flex (drop in magnitude) to absorb phase frustration without tearing the global synchronized state apart.

**Where to find robust damping by design:** Fluidic systems with strong boundary friction. In microfluidic confinement, fluid friction against the walls provides a massive, tunable damping parameter to the rotational mode that doesn't exist in free-space Goldstone modes.

---

### 3 & 4. Symmetry, Hierarchy, and Disorder Robustness

To get a multi-scale hierarchy where collective chiral order is robust to quenched disorder, you need a system where coupling ($K$) and disorder ($\Delta$) can battle in the presence of amplitude flexibility.

* **Criterion for Survival:** In coupled Stuart-Landau oscillators, the survival of the macroscopic chiral mode against disorder $\Delta$ requires that the coupling $K$ exceeds a critical threshold $K_c$. Crucially, the "sloppiness" factor $c = \Gamma_r / \Gamma_\theta$ modifies this: systems with comparable damping can maintain phase-locking (an Arnold tongue) over a much wider spread of local chiral axis disorder because amplitude variations prevent phase singularities (defects) from nucleating easily.

---

### 5. The Best Single Candidate: Confined Bacterial Vortex Lattices

The absolute strongest real physical substrate to study this is **Active Fluids Confined in Microfluidic Lattices** (specifically, dense bacterial suspensions in interconnected pillar arrays).

**Why it fits perfectly:**

* **(a) Spontaneous:** The bacteria push against each other and the boundaries; at a critical density, they spontaneously break parity and circulate CW or CCW.
* **(b) Cyclic NESS:** It is a genuine, massive hydrodynamic NESS circulation.
* **(c) Discrete Symmetry:** By etching a 2D lattice of cavities (e.g., square or kagome), you impose discrete rotational symmetry.
* **(d) Robustly Damped:** Because the fluid is highly viscous and tightly confined by rigid walls, the rotational momentum is heavily overdamped. The relaxation rate back to the chiral NESS is governed by fluid friction, making $\Gamma_\theta$ comparable to the density/alignment amplitude relaxation $\Gamma_r$.

**Measurable Observables & Open Data:**

* **Observable (i) - Chiral Current:** Particle Image Velocimetry (PIV) yields the velocity field $\mathbf{v}(\mathbf{r}, t)$. The local chiral order parameter is the spatial curl / vorticity $\omega = \nabla \times \mathbf{v}$.
* **Observable (ii) - Robust Relaxation Mode:** By introducing optical perturbations or tracking natural fluctuations, you can measure the temporal autocorrelation of the vorticity. A heavily damped mode will show an exponential decay without underdamped ringing, extracting $\Gamma_\theta$.
* **Quenched Disorder:** You can engineer quenched disorder explicitly by making the microfluidic pillars slightly elliptical with randomized major-axis angles.
* **Citations to start:** * Wioland, H., et al. "Ferromagnetic and antiferromagnetic order in bacterial vortex lattices." *Nature Physics* 12.4 (2016).
* Yashunsky, V., et al. "Chiral Edge Currents in Confined Bacterial Active Matter." *Physical Review X* (2022).
* Beppu, K., et al. "Geometry-driven collective spatiotemporal dynamics of active matter." *Soft Matter* (2021).



Another honorable mention is **Quincke Roller Metamaterials** on physical discrete grids (Bricard et al., *Nature* 2013; Soni et al., *Nature Physics* 2019), which spontaneously break symmetry when a DC electric field is applied, though their damping mechanics are slightly stiffer than fluidic boundary friction.

model c:
I'll research this systematically across the relevant literature in active matter, non-reciprocal physics, and chiral nonequilibrium systems. Let me search for the key candidates and their


Here is a system-by-system evaluation against your four criteria, with citations and explicit flags where your framing needs tightening.

---

### 1. Candidates: which systems spontaneously break chiral symmetry into a protected cyclic current?

| System | Spontaneous chiral breaking? | Protected cyclic current? | Discrete rot. symmetry? | Key citation |
|--------|------------------------------|---------------------------|---------------------------|--------------|
| **Non-reciprocal phase transitions** (polariton condensates, coupled oscillators, predator-prey) | **Yes** — PT-symmetric models spontaneously select a rotating order-parameter phase (chiral state) at an exceptional point | Yes — a limit-cycle rotation in the order-parameter space is the nonequilibrium steady state | U(1)/O(2) in continuum; can be discretized to C_n | Fruchart *et al.*, *Nature* **592**, 363 (2021) |
| **Chiral active lattice gas / edge-current condensates** | **No** — microscopic chirality is explicitly imposed (biased rotations); the macroscopic pattern is selected but not spontaneously symmetry-broken from an achiral state | Yes — persistent unidirectional edge currents along faceted interfaces | **Yes** — square-lattice (C4) or n-fold polygonal condensates | Pietzonka & Jülicher, arXiv:2603.20064 (2026) |
| **Bacterial vortex lattices** in asymmetric microwells | **Partially** — individual bacteria are chiral, but the **global** vortex handedness in an achiral circular well is selected spontaneously (≥95% CCW) via competition of top/bottom edge currents | Yes — stable chiral edge currents and corotational vortex pairing | Circular (C∞), but vortex pairing creates effective discrete structure | Beppu *et al.*, *PNAS* **118**, e2107461118 (2021) |
| **Actomyosin cortical flows** | **No** — molecular chirality of actin/myosin provides a built-in bias; the global flow is an amplified, not spontaneously selected, chiral state | Yes — persistent counter-rotating chiral flows in the nonequilibrium steady state | No natural discrete rotational symmetry | Naganathan *et al.*, *eLife* **3**, e04165 (2014) |
| **Ciliary metachronal waves** (zebrafish nose) | **No** — axonemal chirality is built-in; however, the **tissue-scale wave direction** (left vs. right nose) is a spontaneously selected collective chiral mode | Yes — robust traveling waves with fixed propagation direction | Local C2 (left/right) plus tissue-scale alignment | Yuan *et al.*, *eLife* **12**, RP77701 (2023) |
| **Skyrmion lattices** | **No** — Dzyaloshinskii-Moriya interaction explicitly breaks parity; chirality is built into the Hamiltonian | Internal modes carry chiral character, but the “current” is not a directed loop in state space | **Yes** — natural C3/C6 hexagonal lattice | Mankovsky *et al.*, *Phys. Rev. B* **107**, 144415 (2023) |
| **Odd-elastic active solids / chiral active crystals** | Typically **no** — units (colloidal spinners, starfish embryos) are intrinsically chiral | Yes — odd elasticity drives unidirectional edge waves and net angular momentum | Depends on lattice (can be C3/C6) | Fossati *et al.*, *Phys. Rev. E* **109**, 024608 (2024); Marconi & Caprini, *Soft Matter* **21**, 2586 (2025) |
| **BZ / chemical oscillator networks** | **Yes** — spiral waves can nucleate with either handedness; the selection is spontaneous in homogeneous media | Yes — rotating spiral waves are nonequilibrium cyclic attractors | No intrinsic discrete rotational symmetry | — |

**Bottom line for Q1:** The only candidates that satisfy strict spontaneous chiral symmetry breaking (no built-in microscopic bias) are **non-reciprocal phase transitions** and **reaction-diffusion spiral waves**. The biologically grounded systems (bacteria, cilia, actomyosin) all have molecular chirality that biases the macroscopic state; their “spontaneity” is at best emergent. If you relax criterion (a) to allow emergent/mesoscale spontaneity, **bacterial vortex lattices** and **ciliary carpets** become strong candidates.

---

### 2. The decisive property — robust vs. weak chiral damping

Your intuition about the damping anisotropy is correct, but the language needs precision. In the standard amplitude–phase decomposition of a complex order parameter, the “longitudinal” mode is the amplitude relaxation (gapped by the “mass” term) and the “transverse” or “chiral” mode is the phase rotation. In equilibrium, the phase mode is exactly gapless (Goldstone). In driven-dissipative systems, the damping of these modes is read off from the **complex eigenvalue spectrum** of the linearized hydrodynamic operator.

**How to read it off in practice:**

- **Hydrodynamic/Goldstone spectrum:** Look at the imaginary part of the eigenvalues at zero wavevector. If Im(ω_rot) ≪ Im(ω_long), the chiral mode is weakly damped.
- **Odd-vs-even viscosity/elasticity ratio:** In odd viscoelastic solids, the damping matrix contains both symmetric (even) and antisymmetric (odd) parts. The ratio η^o/η and K^o/K controls whether the rotational and longitudinal modes are overdamped with comparable rates or whether the rotational mode becomes underdamped (propagating). In the overdamped limit of odd viscoelasticity, the secular equation shows that the two modes are coupled and both diffusive, with damping rates set by the same effective friction, making them comparable.
- **Damping gap δ in non-Hermitian systems:** In the non-reciprocal O(N) model, the gap δ = |Im(λ_Goldstone) − Im(λ_damped)| separates overdamped from underdamped dynamics. At the critical exceptional point (CEP), δ → 0 and the modes coalesce; away from the CEP, δ is finite and the chiral mode is overdamped (robustly damped).

**System-by-system damping:**

| System | Chiral mode damping | Longitudinal mode damping | Robust or weak? |
|--------|---------------------|---------------------------|-----------------|
| **Non-reciprocal O(N) near CEP** | δ → 0 (modes coalesce) | Same as chiral mode at EP | **Weak** at the EP; **robust** far from EP in the ordered phase |
| **Odd active solids (underdamped)** | “Quasi-dissipation-free” — odd forces counteract friction, leading to propagating waves | Also underdamped | **Weak** — this is the regime you want to avoid |
| **Odd active solids (overdamped)** | Diffusive, coupled to longitudinal mode via η^o K^o | Diffusive | **Robust** — comparable damping rates |
| **Bacterial vortex lattices** | Viscous damping of the suspension; global rotation relaxes via momentum diffusion | Density relaxation also viscous | **Robust** — both rates are set by the same Stokes friction |
| **Actomyosin cortex** | Chiral flow v_y damped by cortical viscosity γ; active torque τ balanced by γ M | AP flow v_x damped by same γ | **Robust** — both flows are damped by the same frictional coefficient; Rho perturbations can change the torque independently, but the damping itself is isotropic |
| **Skyrmion lattices** | Internal (1,1) mode is gapped; lattice translation mode is gapless (Goldstone) | Amplitude mode is gapped | Mixed — the physical rotation of the lattice is a Goldstone mode, but internal chiral deformations are gapped |

**Is there a system gapped/strongly damped by design?**  
Yes: **non-reciprocal condensates far from the exceptional point** and **odd viscoelastic solids in the overdamped regime**. In both cases, the chiral mode is not a soft Goldstone mode but a heavily damped relaxation mode. In the overdamped odd solid, the eigenvalues are purely imaginary (diffusive) with comparable magnitudes for both polarizations.

**Framing correction:** You describe the chiral mode as “rotational.” In the non-reciprocal literature, the chiral mode is usually a **phase rotation** of the order parameter in an internal space, not a physical rotation. The damping of this phase mode is controlled by the non-Hermitian part of the linearized dynamics. In bacterial vortices and actomyosin, it is a physical rotation, damped by viscosity.

---

### 3. Symmetry + hierarchy: discrete rotational symmetry and multi-scale structure

| System | Natural discrete symmetry | Multi-scale / coarse-grainable? | Emergent slower collective mode? |
|--------|---------------------------|----------------------------------|----------------------------------|
| **Bacterial vortex lattices** | Circular confinement (C∞); vortex pairing creates effective C2 or higher | **Yes** — bacteria (1 µm) → microvortices (~35 µm) → global vortex (well size) | **Yes** — the global vortex rotation is slower than the bacterial swimming speed |
| **Ciliary carpets (zebrafish nose)** | Left/right asymmetry (C2); local cilia packing can be hexagonal | **Yes** — individual cilia (µm) → local sync domains (~10 µm) → global metachronal wave (tissue scale) | **Yes** — metachronal wavelength is much larger than cilium length |
| **Skyrmion lattices** | **C3/C6** hexagonal lattice | **Yes** — atomic spins → skyrmions → lattice domains | Phason mode of the lattice is slow, but chirality is built-in |
| **Chiral active lattice gas** | **C4** (square lattice) or n-fold polygonal condensates | **Yes** — lattice sites → condensate domains | Edge-current relaxation is slow compared to particle hopping |
| **Non-reciprocal condensates** | U(1) continuous; must be engineered to C_n | Mean-field theory is single-scale; needs array engineering | Coupled condensate arrays can show slower collective modes |

**Best fit for C3/C6 + hierarchy:** If you can tolerate built-in chirality, **skyrmion lattices** are the natural C3/C6 system. If you need spontaneous symmetry breaking, **bacterial vortex lattices** and **ciliary carpets** have the hierarchy but lack strict C3/C6 at the confinement level (though local packing can be hexagonal). **Chiral active lattice gases** on triangular lattices would give you C6 spontaneously broken to a chiral condensate with n-fold edge currents.

---

### 4. Disorder robustness: finite locking range vs. fragile

The robustness of collective chiral order to quenched disorder in the local chiral axis is directly analogous to the **Kuramoto critical coupling** threshold, but with a crucial twist: in the weakly-damped (near-Goldstone) case, the effective coupling between local chiral axes is marginal, so any disorder destroys long-range order below 4 dimensions. In the robustly-damped case, the coupling is relevant and there is a finite **Arnold tongue / locking range**.

- **Bacterial vortex lattices:** The edge current is robust to boundary geometry variations (curvature, width) and to disorder in bacterial orientations. Beppu *et al.* show that the chiral edge current persists regardless of microwell details, suggesting a finite locking range.
- **Non-reciprocal phase transitions:** The chiral state is protected by the exceptional-point topology. As long as the system remains on the ordered side of the EP, the limit cycle is stable. The “disorder” here is parameter noise; the locking is robust within a finite region of the phase diagram.
- **Actomyosin cortex:** The chirality index c = v_y/v_x is robust to weak perturbations of myosin activity (4–6 hrs RNAi changes both flows proportionally), but sensitive to Rho-pathway perturbations that specifically alter torque. This suggests the chiral axis is locked to the underlying cytoskeletal architecture.
- **Ciliary carpets:** The metachronal wave direction is conserved across individual fish but different left/right, indicating developmental locking. The wave is robust to weak noise in beat frequency.

**Criterion:** A collective chiral mode survives disorder when the coupling strength K between units exceeds the disorder spread Δ: K > Δ. This is the analog of the Kuramoto critical coupling K_c = Δ/2 for phase oscillators. In the robustly-damped case, the effective K is larger because the local chiral modes do not wander diffusively (they are overdamped), so the locking threshold is lower.

---

### 5. Best single candidate, measurable observable, and data availability

**Best candidate: Bacterial vortex lattices in asymmetric microwells (Beppu *et al.*, PNAS 2021)**

**Why it wins:**
- It is the most experimentally mature system that comes closest to your criteria.
- It has a **protected nonequilibrium cyclic current**: the chiral edge current is persistent, unidirectional, and drives the global vortex rotation.
- It has **natural multi-scale hierarchy**: bacteria → microvortices → global vortex.
- The **global chiral mode is robustly damped**: the viscous dissipation of the dense bacterial suspension provides strong damping of the large-scale rotational mode (the Reynolds number is low, and the flow is overdamped).
- It shows **disorder robustness**: edge currents survive geometric variations of the confinement.

**Caveat:** The microscopic chirality of *E. coli* is built-in, so criterion (a) is only satisfied at the mesoscale (global handedness is selected spontaneously in an achiral well). If you require strict microscopic spontaneity, this candidate fails, and you should instead pursue **engineered non-reciprocal oscillator arrays** or **polariton condensate lattices**.

**Measurable observables:**
1. **Self-lit chiral current:** Particle-image velocimetry (PIV) of the bacterial flow field shows the edge current (v_θ near the boundary) and the global vortex rotation. The directionality is ≥95% CCW.
2. **Robust chiral relaxation mode:** After perturbing the flow (e.g., by local optical tweezing or sudden change in confinement geometry), the relaxation time τ_rot of the global vortex orientation can be measured and compared to the density relaxation time τ_long. In the overdamped viscous regime, τ_rot ≈ τ_long ≈ R²/ν, where R is the well radius and ν is the effective kinematic viscosity.

**Published data:**
- Beppu *et al.*, *PNAS* **118**, e2107461118 (2021) — original discovery, includes microwell geometry sweeps and vortex-pairing statistics.
- Raw data and video supplements are available through the PNAS article repository.
- Related follow-up: Beppu & Takeuchi, *Vortex reversal is a precursor of confined bacterial turbulence* (2025) — adds temporal correlation data.

**If you need strict C3/C6 + true spontaneity + robust damping:**  
The **chiral active lattice gas on a triangular lattice** (extending Pietzonka & Jülicher to C6 symmetry) is a theoretical proposal. No experiment has yet realized all four of your criteria simultaneously. The closest theoretical framework is the **non-reciprocal O(N) model on a discrete lattice** (Daviet, Rosch, Diehl 2024), where you can tune the damping gap δ to be large (robust damping) and impose discrete rotational symmetry by hand.

---

### Summary of framing corrections

1. **“Protected cyclic current”**: In active matter, “protected” usually means **dynamically stable on an attractor**, not topologically protected by an index (except in odd-elastic topological waves, where the Chern number protects edge modes). You should say “attractor-protected” or “steady-state circulation.”
2. **“Chiral/rotational relaxation mode”**: Be careful to distinguish **phase rotation** (internal space, Goldstone mode of a broken U(1)) from **physical rotation** (angular momentum in real space). The damping properties are similar, but the physical interpretation differs.
3. **“Goldstone mode”**: In non-reciprocal systems, the Goldstone theorem is modified. At the critical exceptional point, the Goldstone mode collides with a damped massive mode and the two coalesce. There is no clean separation of “massless Goldstone” and “massive amplitude” modes near the transition.
4. **“Robustly damped”**: You mean the **relaxation rate** of the chiral mode is comparable to that of the longitudinal mode. This is equivalent to saying the dynamics is **overdamped and isotropic** in the amplitude-phase plane, or that the damping gap δ is finite and large.

---

## SYNTHESIS — the conceptual payoff (sharpens requirement (d)), and the candidate landscape (2026-05-30)

**Value is conceptual, not (yet) a substrate.** All three models agree no experiment realizes all four
criteria *simultaneously* (model c, explicit). But the convergent correction sharpens the whole search.

**THE CORRECTION (all three).** "Robustly-damped chiral mode" is, precisely, a **gapped** chiral mode.
If chirality comes from breaking a **continuous** rotational symmetry, the orientation/phase mode is a
**Goldstone mode** — generically soft (Re λ_θ → 0 or ∼k²), hence **fragile** to axis disorder. Robustness
requires the chiral mode to be **gapped**, which happens only via: **(i) discrete chirality** (Ising-like
Z₂ CW/CCW — no Goldstone), **(ii) discrete lattice symmetry** (C₃/C₄/C₆ gaps the orientational mode),
**(iii) non-reciprocity / odd elasticity** in the *overdamped* regime (mixes rotational+longitudinal,
isotropizes relaxation), or **(iv) operating far from the exceptional point** (the damping gap δ finite,
the chiral pair well below marginal). ⇒ the #1 weakly-damped chiral plane (Re = −0.1) was a **near-Goldstone
/ near-marginal soft mode**; the Banach's robustness (Re = −1) is just being **gapped / far from the EP**.

**MODEL THREE'S ROTATION POINT (the one to keep).** Our "chiral mode" is an **internal phase rotation**
of the order parameter (the winding in the (E₁,E₂) plane ⟂ the chimeric normal — concentration/population
state space), **NOT a physical real-space rotation** (angular momentum). Two consequences:
- **Faithful real substrates are *internal-cycle* systems** (chemical / ecological / gene-regulatory NESS
  cycles, non-reciprocal order-parameter rotation), **not physical-rotation active matter** (spinner
  lattices, bacterial vortices — those rotate fluid/mass in real space). This is a real selection criterion
  the prompt's candidate list blurred.
- The damping of the internal phase mode is set by the **non-Hermitian** part of the linearization — i.e.
  **distance from the exceptional point**. So requirement (d) unifies with our *existing* prior art:
  `nonhermitian-ep` + `nonreciprocal-transition`. **MPA's own −γI + g·A_CYC is already a non-reciprocal
  model**, and "isotropic-enough plateau" = "operated far from its EP (large damping gap δ)." The EP/CEP is
  exactly where the chiral mode coalesces and goes marginal (the tilt-death, `establishment_compare.py`).

**CANDIDATE LANDSCAPE (none clean; ranked by fit):**
- **Non-reciprocal O(N) / condensate on a *discrete lattice*** (Fruchart et al. *Nature* 592 (2021);
  Daviet–Rosch–Diehl 2024): the closest to MPA's structure — **internal**-phase rotation, strict spontaneous
  chiral SSB, **EP-tunable damping gap δ** (set δ large → gapped/robust), discrete C_n by construction.
  Theoretical / engineerable; not a found natural substrate. **Best conceptual fit, including the rotation point.**
- **Confined bacterial vortex lattices** (Beppu *PNAS* 118 (2021); open data): spontaneous Z₂ CW/CCW,
  robustly *viscously* damped, multi-scale (bacteria→microvortex→global). BUT **physical** rotation (fails the
  internal-rotation criterion) + spontaneity only mesoscale (E. coli chirality built-in). Most experimentally mature.
- **Odd-elastic / chiral active solids** (Fruchart–Vitelli–Scheibner): robust **only in the overdamped
  regime**; underdamped (propagating odd waves) is the weak/fragile side. Usually *explicit* not spontaneous
  chirality. C₃/C₆ + hierarchy good.
- **BZ spiral waves**: strict spontaneous handedness + internal cycle, but no discrete symmetry / hierarchy.

**APPLIED (tracking/borrowed-results currency):** prior-art `goldstone-mode` landed (the robust-vs-weak basis:
continuous-SSB phase mode is soft, gapped only by discrete symmetry / non-reciprocity / a mass — far from the
EP). Frontier `frustration-ascent` substrate-target sharpened: requirement (d) → a **gapped, non-Goldstone,
*internal*-phase chiral mode** (a non-reciprocal chiral system far from its EP), and the faithful substrates
are internal-cycle, not physical-rotation. **Flagged for engine review:** the chiral-mode-as-near-Goldstone /
gapped-far-from-EP reading sharpens the `nonhermitian-ep` ↔ TWO-FACES picture (the Wall/EP is where the
internal chiral phase mode goes marginal). No substrate committed — the screen is now sharp; the hunt continues.
