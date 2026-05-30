Good — order set: (1) formalize the plateau-ladder now, then (2) the observable, then (3) the chaos test. And I'll write you research/prediction prompts where outside models genuinely help.

Let me do Option 1 — move `wall-as-type-boundary` steeping→sharpening with the plateau-ladder framing. It's a frontier-entry relocation, so I'll read the exact current text first to anchor the edits cleanly.

I have the exact text. Removing the steeping entry, then adding the rewritten plateau-ladder entry to the SHARPENING section:

Let me verify the relocation is clean — `wall-as-type-boundary` should now appear once, in the SHARPENING section, with no stray blank line left in STEEPING.

`wall-as-type-boundary` now sits in SHARPENING (line 71), STEEPING is clean (fractional-operator → two-reframe, consecutive). The line-69 hit is the cross-reference inside `frustration-ascent`. Let me confirm the new entry is well-formed and not duplicated:

Option 1 is landed. The relocation is clean — `frustration-ascent` (69) → blank → the new `wall-as-type-boundary` **[sharpening]** entry (71) → blank → BATTERY (73), and STEEPING closed up with no gap. The entry now carries the full plateau-ladder framing, the three-boundary taxonomy on the TWO FACES, the conditional closure-loss scoping, and real `↑`/`✗`/`→` gates.

Let me record the reframe in memory, then write you the research prompt — because the next step (Option 2, the observable) lands best if it sits on the established diagnostic, exactly the way Part C's lift landed on the EP because the establishment pass had mapped it first.

Here's the research prompt — framing-neutral (no MPA jargon the outside model won't know), structured so its answers feed straight into Option 2 (the diagnostic) and Option 3 (the chaos test). Same move that worked for Part C: let the establishment pass map the territory before we build on it.

---

> **I'm studying a hierarchical (multiscale) driven-dissipative dynamical system built by repeated coarse-graining, and I want to know where the established literature already owns the structure I'm seeing, plus the best diagnostics and some predictions. Please answer with specific named results/theorems and citations, and flag where my framing is non-standard or wrong.**
>
> **SETUP.** A driven-dissipative system is coarse-grained level by level. At each level the fast modes relax onto a low-dimensional attractor — empirically always the same normal form (a damped two-mode "breathing + rotation" kernel). So the hierarchy is a **ladder of fixed points of the coarse-graining (renormalization) map**, one per level; the level-to-level map is a contraction (leading eigenvalue ε < 1) onto each fixed point. A **topological invariant** — the cycle-space dimension / the chiral winding sign of a directed 3-cycle in the coupling graph — is **preserved as you move up the ladder** (it does not renormalize away).
>
> I call each fixed point a **plateau** and the transitions **boundaries**. I see three boundary types:
> **(i)** an order-parameter **onset** (pitchfork / transcritical) that turns a level's mode on — I've matched this to a mean-field pitchfork (K_c = c, exponent ½);
> **(ii)** a **sign reversal** of the chiral/winding invariant, forced through a degenerate (balanced) state at a quantized cost;
> **(iii)** a **closure-loss**: the coarse-graining map's leading eigenvalue → 1, the spectral gap closes, and I conjecture the low-dimensional normal-form description breaks down into high-dimensional chaos.
>
> **QUESTIONS.**
> **1. Established homes.** Is "a ladder of RG/coarse-graining fixed points, each a contraction onto the same normal form, with a preserved topological invariant, bounded by an onset bifurcation below and by loss of the spectral gap above" a recognized structure? Candidates to confirm or correct: Wilsonian RG fixed-point sequences + crossover scaling; normally-hyperbolic invariant manifolds + Fenichel theory; center-manifold / slow-manifold reduction towers; Haken synergetics / slaving. What is the right name for boundary (iii) — "loss of normal hyperbolicity"? Fenichel/slow-manifold breakdown? — and is "spectral gap of the reduction map closing → onset of chaos" a standard picture?
> **2. Best diagnostic.** What is the cleanest **computable** observable to distinguish a normally-hyperbolic plateau from a closure-loss boundary in a *simulated* system? (Candidates: spectral gap of the monodromy/reduction operator; full Lyapunov spectrum; covariant-Lyapunov-vector angles / hyperbolicity index; finite-time Lyapunov fluctuations.) I specifically need a diagnostic that does **not** false-positive on a smooth quasiperiodic torus — a positive finite-time-Lyapunov tail on a torus is just non-uniform flow speed, not chaos.
> **3. Chaos route — predictions.** For a chain of N coupled limit-cycle oscillators, compare two couplings: **(a)** instantaneous diffusive nearest-neighbour coupling; **(b)** delayed **negative self-feedback** per oscillator (Mackey-Glass / Hayes type) with gain K and local damping γ.
> – Is it established that (a) tends to synchronize / sit on a low-dimensional torus, while (b) routes to chaos at **N=1** once K > γ and the delay is long enough?
> – Does chaos onset in case (b) depend on N (tower height), or only on the delay and gain?
> – The Ruelle–Takens–Newhouse expectation is "N ≥ 3 incommensurate frequencies → generic strange attractor." In practice, for maximally-incommensurate (golden-ratio-spaced) frequencies with weak diffusive coupling, is the 3-torus actually **robust (KAM)** rather than breaking to chaos? Is "N≥3 → chaos" generic or fragile here?
>
> **Please give named results + citations, and correct any place where my mapping is loose.**

---

Two notes on where this leaves us:

- **The Option-1 frontier edit is uncommitted**, held in the working tree on purpose — Options 2 and 3 will touch the same entry, so I'll commit the `wall-as-type-boundary` refinement as one coherent unit when the thread reaches a natural stop (or on your word).
- **Recommended sequencing:** fetch Q1/Q2 before I build Option 2. The observable should land on the established diagnostic (Q2) rather than a guessed one — that's exactly why Part C's lift cleanly hit the EP: the establishment pass had already named it. Q3 pre-registers predictions for the Option-3 chaos test, which is good falsification hygiene (outside models commit to a prediction before we run it).

When the research comes back, I'll build Option 2's observable on whatever Q2 names as the cleanest plateau-vs-closure-loss diagnostic.


model a:

This is a surprisingly coherent synthesis. The closest established picture is not one single theory, but an overlap of:

1. renormalization-group fixed-point structure,
2. invariant-manifold reduction,
3. pattern-formation/synergetics,
4. topological dynamical systems,
5. delayed-feedback chaos theory.

A few pieces of your terminology are slightly nonstandard, but most of the geometry has recognizable counterparts.

# 1. Where does this structure already live?

## A. "Ladder of fixed points connected by coarse-graining"

This is closest to **RG flows with crossover between fixed points**.

In Wilsonian RG, one normally thinks of a trajectory flowing between fixed points as scale changes. However there are many systems where one encounters:

* a sequence of effective fixed points,
* each governing a finite scale range,
* separated by crossover regions.

Classic references:

* Kenneth Wilson, RG and critical phenomena.
* Leo Kadanoff.
* crossover scaling theory (Fisher, Wegner).

The difference is that RG normally has one flow and several fixed points in parameter space, whereas your description sounds more like:

> each coarse-grained level possesses its own attracting reduced model.

That sounds less like pure RG and more like a hierarchy of invariant manifolds.

---

## B. Same normal form appearing repeatedly

This is extremely reminiscent of:

* center-manifold theory,
* inertial manifolds,
* slaving principle,
* normal-form universality.

The key references are:

* Neil Fenichel
* David Ruelle
* Floris Takens
* Hermann Haken

Haken's language is especially close.

His picture:

* unstable modes become order parameters,
* fast modes are slaved,
* reduced dynamics follows a universal normal form.

Your "breathing + rotation kernel" sounds very much like repeated appearance of the same low-dimensional center-manifold normal form.

The word "plateau" is your own terminology, but mathematically I would translate:

> plateau = normally hyperbolic reduced attractor carrying a universal normal form.

---

## C. Preserved chiral/cycle invariant

This is where the structure becomes less classical.

If the invariant truly survives coarse-graining, then the closest analogies are:

* topological phases,
* homology persistence,
* Conley index continuation,
* topological RG invariants.

In particular:

* cycle-space dimension = first Betti number,
* winding sign = orientation/chirality class.

These are exactly the sorts of objects that often survive coarse-graining.

The analogy to topological phases is strong:

local details renormalize away,
global topological information survives.

That part of your picture is not strange at all.

---

# 2. What is boundary (iii)?

Your candidate:

> leading eigenvalue → 1
>
> spectral gap closes
>
> reduced model ceases to close

is almost textbook.

The standard name is:

### Loss of normal hyperbolicity

Fenichel's theorem requires:

* tangent dynamics weak,
* transverse contraction stronger.

Schematically:

[
|\lambda_{\rm tangential}|
<
|\lambda_{\rm transverse}|.
]

When transverse contraction vanishes,

[
\lambda_{\rm transverse}\to 0
]

(continuous time)

or

[
|\mu_{\rm transverse}|\to 1
]

(discrete-time map),

normal hyperbolicity is lost.

That is exactly the condition under which Fenichel persistence fails.

So your closure-loss boundary is most naturally:

> loss of normal hyperbolicity of the reduced manifold.

---

## Important correction

The statement

> spectral gap closes → chaos

is **not generally true**.

What is true is:

spectral-gap closure
→ loss of reduction validity.

After that several things may happen:

* another attractor,
* torus bifurcation,
* intermittency,
* crisis,
* chaos,
* higher-dimensional quasiperiodicity.

Chaos is only one possibility.

A better statement is:

> spectral-gap closure is necessary for breakdown of the reduction but not sufficient for chaos.

---

# 3. Best diagnostic

You want:

> distinguish NHIM plateau from closure-loss boundary
>
> without false-positives on quasiperiodic tori.

I would not use finite-time Lyapunov tails.

You already identified the problem.

A torus can show large FTLE fluctuations while remaining perfectly nonchaotic.

---

## Best single observable

Measure the smallest transverse Lyapunov exponent.

For a NHIM:

[
\lambda_{\perp}<0.
]

At boundary:

[
\lambda_{\perp}\to 0.
]

That is almost the definition of loss of normal hyperbolicity.

---

## Better practical observable

Use covariant Lyapunov vectors (CLVs).

Reference:

* Francesco Ginelli

Monitor:

[
\theta_{\min}
=============

\text{minimum angle between stable and unstable bundles}.
]

Hyperbolic systems:

[
\theta_{\min}>0.
]

Loss of hyperbolicity:

[
\theta_{\min}\to 0.
]

This is one of the cleanest known diagnostics.

---

## Gold-standard test

Use both:

1. spectral gap of transfer/Koopman/Perron-Frobenius reduction;
2. CLV angle statistics.

If both collapse simultaneously, you are probably seeing genuine loss of normal hyperbolicity.

---

# 4. Diffusive coupling versus delayed self-feedback

Here the literature is very clear.

## A. Diffusive coupling

Nearest-neighbor diffusive coupling generally promotes:

* synchronization,
* phase locking,
* low-dimensional collective motion.

Canonical framework:

* Yoshiki Kuramoto
* master-stability formalism of Louis Pecora and Thomas Carroll.

Weak coupling:

* invariant tori survive,
* synchronization develops gradually.

So your intuition is basically right.

---

## B. Delayed negative feedback

Completely different.

A delay equation is infinite-dimensional.

The classical example is:

Mackey-Glass equation

[
\dot x(t)
=========

-\gamma x(t)
+
\frac{\beta x(t-\tau)}
{1+x(t-\tau)^n}.
]

Also:

Hayes equation

A single delayed oscillator can exhibit:

* Hopf bifurcation,
* period doubling,
* chaos,

with no network required.

So:

> can N=1 become chaotic?

Yes.

That is completely established.

---

# 5. Does delayed-feedback chaos depend on N?

Not fundamentally.

The delay already provides effectively infinite-dimensional phase space.

For many delayed systems:

[
N=1
]

is sufficient.

Increasing N adds more modes but is not required for chaos.

The dominant parameters are usually:

[
K,\gamma,\tau.
]

not network size.

This is a major distinction from ordinary ODE oscillator networks.

---

# 6. Ruelle–Takens versus KAM

This is the place where people often overstate the Ruelle–Takens story.

The slogan:

> three frequencies imply chaos

is false.

What Ruelle–Takens actually argued is that:

after sufficiently many Hopf-type additions of frequencies,

generic perturbations tend toward strange attractors.

The word is **generic**, not inevitable.

---

## KAM side

For weak perturbations of integrable systems:

* invariant tori persist,
* especially strongly irrational frequencies.

The golden ratio is the most famous example.

The relevant theory is:

Andrey Kolmogorov,
Vladimir Arnold,
Jürgen Moser.

A 3-torus with sufficiently weak coupling can remain perfectly robust.

So:

> N≥3 → chaos

is not a theorem.

It is at best a heuristic for dissipative systems away from the KAM regime.

---

# My overall translation of your framework

If I were rewriting your description in standard dynamical-systems language, I would say:

> The hierarchy consists of a sequence of normally hyperbolic attracting invariant manifolds generated by repeated coarse-graining. Each manifold carries the same universal low-dimensional normal form. A topological cycle/winding invariant is preserved under renormalization. Lower boundaries correspond to symmetry-breaking bifurcations (pitchfork/transcritical onset). Upper boundaries correspond to loss of normal hyperbolicity, detected by collapse of the transverse spectral gap. Beyond this boundary the reduced description fails and the system may transition to higher-dimensional quasiperiodicity, intermittency, crises, or chaos.

The strongest established anchor for your boundary (iii) is not RG, and not chaos theory directly. It is **Fenichel's theory of normally hyperbolic invariant manifolds and their breakdown**. That's the mathematical object that most closely matches the geometry you've described.

model b:
This is a sophisticated and fascinating setup. Your framing of a multiscale driven-dissipative system as a "ladder" of coarse-graining fixed points is conceptually powerful, though it bridges several distinct mathematical traditions that don't always use the same vocabulary.

Here is a breakdown of where your model lives in the established literature, the best computational diagnostics, and a reality check on your chaos predictions.

---

### 1. Established Homes and Nomenclature

Your mapping is largely correct, but it spans statistical physics and dynamical systems theory. Here is the formal vocabulary and the exact frameworks that "own" your structure:

* **The "Ladder" and the Plateaus:** Your model perfectly describes **Haken's Synergetics** (specifically the **Slaving Principle**) and **Inertial Manifold Theory**.
* In dynamical systems, when fast modes relax onto a low-dimensional attractor, the slaved modes live on a globally attracting, invariant manifold. When this happens sequentially across scales, you are constructing a hierarchy of **Inertial Manifolds** (Foias, Sell, & Temam, 1988).
* Your mapping to Wilsonian RG is a valid physical analogy, but strictly speaking, in dissipative ODEs/PDEs, you are performing sequential **Center Manifold Reductions** (Carr, 1981) or tracking **Normally Hyperbolic Invariant Manifolds (NHIMs)** via **Fenichel Theory** (Fenichel, 1971).


* **Preserved Topological Invariant:** The survival of a chiral/winding invariant through coarse-graining is a very modern concept, belonging to the rapidly growing field of **Topological Non-Hermitian Dynamics** and **Symmetry-Protected Topological (SPT) phases in open systems** (e.g., Gong et al., 2018). In traditional RG, topological terms do indeed survive flow (they are exactly marginal or robustly quantized), but seeing this specifically as a cycle-space dimension in a dissipative coupling graph bridges spectral graph theory and non-Hermitian skin effects.
* **Boundary (iii) – "Closure-loss":** Your terminology "loss of the spectral gap" is good, but the canonical name for this boundary is the **Loss of Normal Hyperbolicity** or **Slow Manifold Breakdown**.
* Fenichel Theory states that an invariant manifold survives *only* as long as the spectral gap condition is met: the contraction rate *towards* the manifold must strictly exceed the contraction/expansion rates *on* the manifold.
* When the leading transverse eigenvalue $\epsilon \to 1$, the spectral gap closes, and the fast modes decouple from the slow modes. "Spectral gap closing $\to$ onset of chaos" is indeed a standard picture, often studied formally as a **Blowout Bifurcation** (Ott & Sommerer, 1994) or **Transverse Instability**, where trajectories are expelled from the invariant manifold into the high-dimensional bulk phase space.



### 2. Best Computable Diagnostic

To distinguish a normally-hyperbolic plateau from a closure-loss boundary without false-positive tripping on a quasiperiodic torus, you should use the **Covariant Lyapunov Vectors (CLVs)** and specifically compute the **Hyperbolicity Index (or angle between Oseledec subspaces)**.

* **Why it works:** Unlike orthogonal Gram-Schmidt vectors (which are basis-dependent), CLVs point along the true stable, neutral, and unstable directions of the local tangent space. On a normally hyperbolic plateau, there is a strict topological separation (a finite angle bounded away from zero) between the tangent subspace (the flow on the low-D attractor/torus) and the stable transverse subspace (the slaved fast modes).
* **The Observable:** Compute the minimum angle $\theta$ between the CLV subspace associated with $\lambda_i \le 0$ (the manifold dynamics) and $\lambda_k < 0$ (the transverse contraction).
* **Avoiding the Torus Trap:** On a smooth quasiperiodic torus, you will have multiple zero Lyapunov exponents ($\lambda = 0$). Finite-time Lyapunov Exponents (FTLEs) will fluctuate and give you false positive "chaos" tails simply due to the phase-space geometry varying the flow speed. However, the *angle* between the neutral directions on the torus and the strongly negative transverse directions will remain bounded away from zero. When normal hyperbolicity is lost (Boundary iii), these subspaces collide (a homoclinic tangency), and $\theta \to 0$.
* **Citation:** The standard, highly efficient algorithm for this in simulated systems is by **Ginelli et al. (2007)** ("Characterizing dynamics with covariant Lyapunov vectors").

### 3. Chaos Route Predictions

Your intuition here is mostly correct, but the exact mathematical guarantees require nuance, especially regarding the Ruelle-Takens-Newhouse (RTN) theorem.

**Instantaneous vs. Delayed Feedback (N=1)**

* **Case (a) Instantaneous Diffusive:** You are correct. Diffusive nearest-neighbor coupling of limit cycles generally leads to phase locking/synchronization (e.g., Kuramoto dynamics) or simple low-dimensional quasiperiodicity.
* **Case (b) Delayed Negative Self-Feedback:** It is a rigidly established fact that a single oscillator ($N=1$) with delayed feedback forms an infinite-dimensional dynamical system (a Delay Differential Equation, DDE). Once $K > \gamma$ and the delay $\tau$ passes a critical threshold $\tau_c$, the system generic routes to high-dimensional chaos.
* **Does N matter for (b)?** For chaos *onset*, $N$ is largely irrelevant. $N=1$ is already infinite-dimensional. Increasing $N$ (tower height) simply scales the maximum possible Lyapunov dimension of the resulting strange attractor, but the local nodal parameters ($K, \tau$) drive the primary instability.
* **Citation:** The foundational demonstration of this is the **Mackey-Glass Equation** (Mackey & Glass, 1977) and Farmer (1982) "Chaotic attractors of an infinite-dimensional dynamical system."

**Ruelle-Takens-Newhouse vs. KAM (N $\ge$ 3)**

* **Your framing:** Is the 3-torus robust (KAM) rather than breaking to chaos? Is "N $\ge$ 3 $\to$ chaos" fragile?
* **The Reality:** The RTN theorem states that an arbitrarily small perturbation to a 3-torus *can* produce a strange attractor. However, this is a topological statement (Baire category), not a measure-theoretic one.
* **Dissipative KAM Theory:** If the frequencies are maximally incommensurate (e.g., golden-ratio spaced) and the coupling is weak, the tori are indeed **robust**. They occupy a set of positive Lebesgue measure in parameter space. The RTN perturbations exist, but they are often confined to microscopically thin Arnold tongues.
* **The Verdict:** In a physical or simulated system, "N $\ge$ 3 $\to$ chaos" is actually the **fragile** concept at weak coupling. The robust 3-torus will dominate your simulation. You typically must crank the coupling strength past a finite threshold to destroy the tori (breaking the Diophantine condition) to observe generic chaos.
* **Citations:** **Grebogi, Ott, & Yorke (1985)** ("Attractors on an N-torus: Quasiperiodicity versus chaos") demonstrates exactly this phenomenon. The theoretical foundation is the **Dissipative KAM Theorem** by Broer, Huitema, & Takens (1990).

---

Since preserving a topological invariant like a chiral winding sign up a coarse-graining ladder is quite exotic for standard dissipative systems—how are you currently tracking or defining this cycle-space dimension numerically as the dimension of the fast modes is integrated out?

model c:



Below is a point-by-point mapping of your structure to named results, plus corrections where your framing deviates from the standard literature.

---

### 1. Established homes for the “plateau–boundary” ladder

**Your core structure** — a hierarchy of coarse-graining steps, each landing on the *same* low-dimensional normal form, with a preserved topological invariant, bounded below by an onset bifurcation and above by a spectral-gap closure — is **not** a standard Wilsonian RG fixed-point ladder in the usual sense. It is closest to a **nested family of Normally Hyperbolic Invariant Manifolds (NHIMs)**, with phenomenological language borrowed from Haken’s synergetics.

| Your candidate | Verdict | Named result / citation |
|---|---|---|
| **Wilsonian RG + crossover scaling** | Partial match only. Standard RG crossover (e.g., Cavagna *et al.* 2019) describes flow *between* two fixed points (conservative → dissipative) as a function of scale. Your “ladder of fixed points, each a contraction onto the *same* normal form” is not the standard Wilsonian picture; Wilsonian RG normally deals with a *single* critical fixed point and its relevant/unstable directions. | Cavagna *et al.*, *Phys. Rev. E* **100**, 062130 (2019) — crossover between unstable conservative and stable dissipative fixed points with exponent κ = 4/d. |
| **Normally hyperbolic invariant manifolds + Fenichel theory** | **This is the rigorous home for your plateaus.** Fenichel (1971–1974) and Hirsch–Pugh–Shub (1977) proved that a manifold M persists under perturbation if it is *r*-normally hyperbolic: the normal contraction/expansion rates dominate the tangential ones by a spectral-gap ratio r ≥ 1 (ρ₋ < −rρ_M ≤ 0 ≤ rρ_M < ρ₊). Your “level-to-level map is a contraction (ε < 1)” is exactly the spectral-gap condition. The “same normal form” at each level is the persistent NHIM of the reduced flow. | Fenichel, *J. Diff. Eq.* **31** (1979); Hirsch–Pugh–Shub, *Invariant Manifolds* (1977); Eldering, *Normally Hyperbolic Invariant Manifolds: The Noncompact Case* (2013) for modern noncompact extensions. |
| **Center-manifold / slow-manifold “towers”** | Conceptually natural, but **no canonical “tower theorem” exists** in the literature. Iterated slow-manifold reduction is done in practice (e.g., in chemical kinetics), but it is not packaged as a named ladder of fixed points. Your construction is a legitimate multiscale extension, but you are extending Fenichel/Haken, not citing an established tower. | — |
| **Haken synergetics / slaving** | Exact phenomenological match. Haken’s slaving principle states that fast (stable) modes are enslaved by slow order parameters; the order parameters obey low-dimensional dynamics. Your boundary (i) “order-parameter onset” is a textbook synergetics bifurcation. | Haken, *Synergetics* (1977, 1983); Scholarpedia “Synergetics”. |

**Boundary (iii): the correct name.**  
“Loss of normal hyperbolicity” is the precise term. “Fenichel breakdown” and “slow-manifold breakdown” are acceptable informal variants. The spectral-gap condition is sharp: when the non-strict inequality ρ_s ≤ rρ_x holds, the persistent manifold can lose differentiability and may cease to persist as a smooth manifold (Eldering, §1.2.1).

**Flag: “spectral gap closing → onset of chaos” is non-standard.**  
The standard picture distinguishes *two* breakdown mechanisms:

1. **Vanishing rates**: Normal Lyapunov multipliers → 1 (your spectral-gap closure). This leads to bifurcations (saddle-node, period-doubling) but not automatically to chaos.
2. **Vanishing angles**: The invariant stable/tangent directions collapse (bundle collapse), while multipliers remain bounded away from 1. This is the “direction-merging” scenario of Haro & de la Llave (2006), which can produce strange nonchaotic attractors or Cantori.

Your conjecture that gap closure *directly* causes high-dimensional chaos is therefore **not a standard theorem**; it is a plausible but unproven scenario. The rigorous literature treats loss of NHIM as a precursor to *possible* complex dynamics, not a guaranteed chaos onset.

---

### 2. Best diagnostic: NHIM plateau vs. closure-loss

**Do not rely on the full Lyapunov spectrum or FTLE alone.**  
On a smooth quasiperiodic torus, finite-time Lyapunov exponents fluctuate because of non-uniform winding; a positive FTLE tail is a false positive. The full spectrum also fails to distinguish a chaotic orbit from a torus when exponents are near zero.

**The cleanest computable observable is the minimum angle between Covariant Lyapunov Vector (CLV) subspaces.**

- **Why it works:** For a normally hyperbolic plateau, the Oseledec splitting (stable ⊕ tangent ⊕ unstable) is *transverse*: the angles between subspaces are bounded away from zero. As normal hyperbolicity is lost via the “bundle-collapse” route, the minimum angle θ_min between the stable and tangent (or fast and slow) bundles collapses to zero. This is a geometric, norm-independent diagnostic.
- **Why it avoids the torus false-positive:** On a smooth quasiperiodic torus that is normally hyperbolic, the CLVs exist and remain transverse; θ_min stays bounded away from zero (except on measure-zero sets). The torus does not produce a systematic tail toward θ = 0.
- **Algorithm:** Ginelli *et al.* (2007) provide the standard algorithm to compute CLVs via forward QR + backward iteration. The hyperbolicity index can be taken as the time-averaged minimum angle 〈θ_min〉 or the fraction of time spent below a threshold θ_c.

**Complementary check:**  
Verify the **dominated splitting** condition: for some finite Δ₀, the local Lyapunov exponents averaged over any window Δ > Δ₀ must not change their spectral ordering. If the ordering is preserved, the splitting is dominated and the manifold is NHIM. If two bundles swap order, the gap has closed.

---

### 3. Chaos-route predictions

**(a) Instantaneous diffusive nearest-neighbour coupling**  
Yes, established: diffusively coupled limit-cycle oscillators typically synchronize or settle on a low-dimensional torus. The weak-coupling limit is described by the Ginzburg–Landau / Kuramoto phase reduction, where phase-locking and quasiperiodic tori are generic. Chaos requires stronger coupling or symmetry breaking.

**(b) Delayed negative self-feedback (Mackey–Glass / Hayes type)**  
- **Mackey–Glass (single variable, N = 1):** The classic result is that a scalar DDE with delayed nonlinear feedback generates chaos once the delay τ exceeds a threshold (τ ≳ 10 in the standard parameter set). Farmer (1982) showed the attractor dimension scales as D ∼ τ/τ_relax (i.e., D ∼ 1/ε). Junges & Gallas (2012) mapped the intricate period-doubling and chaotic routes. **N = 1 is sufficient.**
- **Hayes equation:** The linear Hayes equation ẋ = x − Gx(t−τ) only shows stability boundaries. With nonlinear negative feedback (e.g., the Mackey–Glass nonlinearity or mixed feedback), chaotic dynamics are observed; the 2021 “Resonating Delay Equation” study reports chaos with negative-feedback functions.
- **N-dependence:** For DDEs, the effective phase-space dimension is set by the delay/damping ratio, not by the number of coupled units. **Chaos onset depends primarily on the local delay τ and gain K**, not on the tower height N. Adding oscillators increases dimension but does not change the local chaos threshold.

**Ruelle–Takens–Newhouse vs. KAM robustness of the 3-torus**

- **The RTN theorem** (Newhouse, Ruelle & Takens, *Commun. Math. Phys.* **64**, 35 (1978)): For a quasiperiodic flow on T³, in every C² neighborhood there exists a vector field with a strange Axiom A attractor. For T^m, m ≥ 4, C^∞ perturbations suffice.
- **Is it generic? No — it is fragile.** Grebogi, Ott & Yorke (1985) numerically showed that for small-to-moderate nonlinearity, 3-frequency quasiperiodicity is the *most common* attractor, while chaotic attractors are “extremely uncommon.” The RTN perturbations are nearby in function space but require delicate, non-generic tuning.
- **Dissipative KAM:** Broer, Huitema, Takens & Sevryuk developed dissipative KAM theory proving that quasiperiodic attractors with Diophantine frequencies persist under small perturbations in dissipative systems. Your specified regime — maximally incommensurate (golden-ratio-spaced) frequencies with weak diffusive coupling — falls directly into this dissipative KAM window. The 3-torus is **robust** here.

**Bottom line:** “N ≥ 3 → chaos” is **not generic** in the sense of measure on parameter space; it is a mathematically possible but fragile scenario. For golden-ratio frequencies and weak coupling, the dissipative KAM theorem guarantees torus persistence.

---

### Summary of corrections to your framing

| Your statement | Correction |
|---|---|
| “Ladder of RG fixed points, each the same normal form” | Not standard Wilsonian RG. Rigorous home is **hierarchy of NHIMs**; phenomenological home is **Haken synergetics**. |
| Boundary (iii) = “closure-loss” | Correctly termed **loss of normal hyperbolicity** or **spectral-gap violation**. |
| “Spectral gap closing → onset of chaos” | **Non-standard conjecture.** Gap closing enables bifurcations; chaos is one possible outcome, not guaranteed. |
| FTLE as diagnostic | **False-positive on tori.** Use **CLV angle distributions** instead. |
| “N ≥ 3 incommensurate frequencies → generic chaos” | **Fragile, not generic.** Dissipative KAM makes the 3-torus robust for Diophantine frequencies and weak coupling. |
| Mackey-Glass chaos requires large N | **Incorrect.** N = 1 suffices; dimension is controlled by delay/damping ratio. |