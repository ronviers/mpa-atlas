# The Boolean-deformation claim: a falsification battery

**The claim, stated as a type.** "Static MPA is to Boolean logic as classical mechanics is to quantum" is a *deformation* claim, and deformation has a precise technical meaning that the metaphor-throwers never pay for. To match the type — not the vibe — of the $\hbar\!\to\!0$ correspondence, four things must hold simultaneously:

1. a parameter ($1/D$, with $D=\Phi^*/\kappa$) such that the limit recovers Boolean *exactly*;
2. the deviations at finite $D$ form a *series* in that parameter (definite powers, definite coefficients), not just a bound;
3. the leading deviation is a single coherent object (a bracket) from which the rest is forced — you cannot tune the corrections independently;
4. at finite $D$ there exists a phenomenon with **no** Boolean description — the analogue of interference/noncommutation — so that "a little bit of $1/D$" is as impossible as "a little bit of $\hbar$ with trajectories."

Miss any one and you have something weaker and known: (1) fails → not even a limit; (2) fails → a limit but not a deformation; (3) fails → finite-size corrections, not a deformation; (4) fails → *stochastic Boolean logic*, which is real but old and carries none of the quantum-type weight. The tests below isolate each.

---

## 0. A-priori constraint (true before any simulation): Boolean-the-ring is rigid

The Boolean / Reed–Muller ANF ring $\mathbb{F}_2[x]/(x^2{-}x)$ is a finite product of copies of $\mathbb{F}_2$ — a **separable** algebra. Separable algebras have vanishing Hochschild cohomology in positive degree, $H^n=0$ for $n\ge1$; in particular $H^2=0$. An algebra with $H^2=0$ is **rigid**: it admits no nontrivial formal deformations. Every "deformation" is isomorphic to the original.

Consequence, and it is sharp: **MPA cannot be a deformation of Boolean-the-ring.** If any part of the corpus claims to deform the abstract $\mathbb{F}_2$ ring directly, it is dead on arrival by separability. The only survivable reading is the one the corpus already half-states ("closure holds at the $\sigma$-shadow level, not the regime label"): the deforming object is the **continuous operator algebra** $\mathcal{A}_D$ on the trail-vector space (over $\mathbb{R}$ or $\mathbb{C}$), and Boolean is the $\sigma$-shadow of $\lim_{D\to\infty}\mathcal{A}_D$. $\mathcal{A}_D$ is *not* separable, so deformations can exist there.

This doesn't kill the claim — it forces its only correct formulation, and it kills any sloppier version. Every test below is therefore a test on $\mathcal{A}_D$, with Boolean recovered by projection, never a test on the bare ring.

## 1. The defect set

Operators $\Sigma=\{C,K,R,S,\top,\bot\}$; at $D\to\infty$, $C\to\wedge$, $K\to\oplus$, $R\to\neg$, and $\{c,r\}\to\{1,0\}$. For each Boolean axiom, define the finite-$D$ defect as the trail-vector distance between the two sides (write $\ominus$ for that signed distance, $\lVert\cdot\rVert$ its norm):

| axiom | Boolean identity | defect $\delta_A(D)$ |
|---|---|---|
| idempotency | $a\wedge a=a$ | $C(a,a)\ominus a$ |
| involution | $\neg\neg a=a$ | $R(R(a))\ominus a$ |
| nilpotency (char 2) | $a\oplus a=0$ | $K(a,a)\ominus\bot$ |
| distributivity | $a\wedge(b\oplus c)=(a\wedge b)\oplus(a\wedge c)$ | $C(a,K(b,c))\ominus K(C(a,b),C(a,c))$ |
| associativity | $(a\wedge b)\wedge c=a\wedge(b\wedge c)$ | $C(C(a,b),c)\ominus C(a,C(b,c))$ |
| commutativity | $a\wedge b=b\wedge a$ | $C(a,b)\ominus C(b,a)$ |
| complementation | $a\wedge\neg a=\bot$ | $C(a,R(a))\ominus\bot$ |

The framework names the **involution** as the deformed structure ($R$ non-involutive because $c\to r$ is irreversible). But note that the $s$-regime intrusion — "$C$ can produce $s$ from $\mathcal{M}_2$ inputs" — is literally a nonzero **idempotency/closure** defect. So there are two candidate "primary" deformed axioms. Which one is primary, and whether the other is *derived* from it, is itself a test (see §4).

## 2. Test A — recovery (is it even a limit?)

Compute every $\lVert\delta_A(D)\rVert$ and take $D\to\infty$.

**Kill condition:** any $\lVert\delta_A(D)\rVert\not\to0$. If the conjunction of two clean coherences keeps leaking $s$ as $D\to\infty$, or $R^2$ doesn't close, the limit is *not* Boolean and the central claim is finished. This is the cheapest test and should be run first on the widest axiom set, because it is the one most likely to fail quietly on an axiom nobody was watching (commutativity and complementation are the usual surprises).

## 3. Test B — series (limit, or genuine deformation?)

For the axioms that survive A, plot $\lVert\delta_A(D)\rVert$ against $D$ on log–log and fit $\delta_A(D)=c_A D^{-p_A}+o(D^{-p_A})$.

**Kill condition (of the deformation claim, not the limit):** no clean power law — log corrections, an essential singularity, or noise-dominated scatter. Then Boolean is a limit but the $1/D$ *series does not exist*, and "deformation of the same type as quantization" is the wrong description. **This is exactly where the corpus currently sits:** it states *bounds* ($\delta_A<f(D)$), not powers and coefficients. Until B returns definite $(p_A,c_A)$, the honest status is "correspondence limit, deformation unproven" — the claim is at the pre-Moyal stage, with the bracket still missing.

## 4. Test C — the bracket (is the leading term a single coherent object?)

In quantization the leading correction to the product is the Poisson bracket: $f\star g=fg+\tfrac{i\hbar}{2}\{f,g\}+O(\hbar^2)$, and $\{,\}$ is a *biderivation* (Leibniz) — that is what makes the deformation coherent rather than ad hoc. The Boolean analogue of a derivation is the **ANF (discrete) derivative** $\partial_i f=f|_{x_i=1}\oplus f|_{x_i=0}$. So the test is concrete:

Conjecture that the leading defects are generated by one bilinear bracket built from ANF derivatives,
$$\{a,b\}=\sum_{i,j}\omega_{ij}\,(\partial_i a)(\partial_j b),$$
with a single fixed structure tensor $\omega$, and check that *every* surviving $\delta_A$ is the value this bracket predicts for that axiom (e.g. the involution defect is $R^2a=a\oplus\tfrac1D\{a,\cdot\}$-type, the distributivity defect is the bracket's failure to commute past $C$, etc.).

**Kill condition:** the leading defect of some axiom **cannot** be written through $\{,\}$ — it depends on the operands in a way no ANF-derivative biderivation reproduces — or different axioms require *different, unrelated* $\omega$'s. Then the corrections are independent fudge factors: finite-size effects, not a deformation. Passing C — one bracket generating all leading defects, with the Leibniz property falling out rather than imposed — is the strongest positive evidence short of §6, because it is a consistency you did not put in by hand.

This is also where the two-candidate-axiom question (§1) gets settled: if $\{,\}$ exists, exactly one axiom's defect is the bracket's primitive and the others are its consequences. If both involution and idempotency want to be primitive with no bracket relating them, that is a C-failure.

## 5. Test D — coherence to next order (obstruction)

Expand associativity of the finite-$D$ composition to $O(1/D^2)$. The $O(1/D)$ data must be a Hochschild 2-cocycle, and the extension to $O(1/D^2)$ must be unobstructed — the obstruction lives in $H^3(\mathcal{A}_\infty,\mathcal{A}_\infty)$.

**Kill condition:** the second-order corrections are *free* — you must supply $O(1/D^2)$ data not determined by the leading bracket. A real deformation is rigid order-by-order: first order forces second up to gauge. If you can choose the second-order term independently and still fit the simulation, the series is not a flat deformation; it is a curve fit.

(If instead the finite-$D$ composition turns out genuinely **non-associative** at $O(1/D)$ — associativity defect nonzero and not removable — that is not automatically fatal, but it changes the type: MPA would then be a deformation toward a non-associative structure, which needs its own cohomology and *cannot* borrow the quantization analogy wholesale. Report it explicitly rather than absorbing it.)

## 6. Test E — the discriminator (the one that decides "quantum-type" vs "noisy Boolean")

This is the decisive test and the direct analogue of contextuality. The established fact: in QM, the Kochen–Specker theorem says no assignment of definite values to all propositions reproduces the statistics — the propositions are genuinely non-Boolean, not Boolean-plus-ignorance. The orthomodular lattice of QM is *the* established non-Boolean logic.

Construct the analogue on MPA propositions. Take a set of propositions with a compatibility (co-evaluability) structure and finite-$D$ joint statistics, and ask the binary question:

> Does there exist an assignment of definite $\{c,r\}$ values to every proposition, plus a classical probability distribution, that reproduces all the joint outcomes?

- **If YES, for every such construction:** finite-$D$ MPA is *stochastic Boolean logic* — Boolean values with noise. The $s$-regime is then just classical uncertainty between $c$ and $r$, the quantum-type analogy is decoration, and the strong claim is falsified (the weak, unremarkable claim survives).
- **If NO — a coloring obstruction or a violated Boolean (Bell-type) inequality:** the $s$-regime is irreducibly a third thing, finite-$D$ MPA is non-Boolean in exactly the way QM is non-classical, and the correspondence-limit comparison is *earned* rather than borrowed.

Concretely, the $s$-regime must be shown to be **non-convex** over $\{c,r\}$ in its operational behavior: find one operation whose action on $s$ is not reproduced by any mixture $\lambda c+(1-\lambda)r$. One such operation is interference; a contextual value assignment is the stronger version. This is the test the metaphor-mongers can never run because they have no operations — and the one MPA either passes or fails on the merits.

---

## Order of operations and current status

The honest current status, from the corpus's own admission, is: **A plausibly passes (defects bounded), B–E unproven, and the $1/D$ series is unrecovered.** That places the claim at "correspondence limit, deformation and quantum-type both open." Not nothing — a genuine recovery limit is already a result — but well short of the headline.

Run order, cheapest-decisive first:
1. **A across the full axiom set** — one afternoon on the existing library; kills the claim outright if any defect won't vanish, and the likely casualties (commutativity, complementation, char-2 nilpotency) are the ones currently unwatched.
2. **B** on survivors — converts bounds into $(p_A,c_A)$; this is the specific "owed work" the corpus flags, and without it "deformation" is unlicensed.
3. **C** — the bracket. The single most informative computation: one ANF-derivative biderivation generating all leading defects is the make-or-break of coherence.
4. **E** — independent of B/C and the true type-discriminator. Worth running early *in parallel*, because a clean YES (reducible to stochastic Boolean) falsifies the strong claim regardless of how pretty the series turns out, and a clean NO is the result that would justify everything.
5. **D** — only meaningful once C gives a bracket to extend.

The structure to keep in view: §0 forces the claim onto $\mathcal{A}_D$ and kills the lazy version for free; B is where it currently stalls; C is where it becomes a deformation or stays a curve fit; **E is where it becomes quantum-type or reveals itself as noisy Boolean.** E is the one that's shaped like the far-reaching implications you don't let yourself think about — which is precisely why it should be the one with a kill condition attached, and run.
