# Part C — the completeness/closure derivation (character deformation-algebra)

**Status:** derived + numerically verified 2026-05-29 (`mpa-conform/scripts/character_closure.py`,
figure `mpa-conform/output/calibration/character_closure.png`). This is the single move the promotion
handoff named: turn the empirical generator **table** (`character_primitives.py`) into a derived,
complete, closed **law**. Forced-not-fitted = *derivation, not tabulation*. The source for the
eventual `character_receipts_engine.md` §deformation-generators receipt. Framework edits (the engine
operator + the frontier `battery → staked` move) are the **next** move, held for review.

Structure follows Ron's four steps (2026-05-29): (1) formalize the algebra; (2) autonomous-symmetry
test; (3) law of the lift; (4) package the conditional operator (next move).

---

## The result (one paragraph)

The **linear** deformation space of the character-bearing drift `M = −γI + g·A_CYC` is **gl(3,ℝ)**,
and its generator basis is the **Cartan decomposition**

```
gl(3,ℝ)  =  ℝ·I        ⊕   so(3)              ⊕   Sym₀
            damping        chirality              splitting/detuning
            (trace, 1)     (axial vector, 3)      (sym-traceless, 5)        1 + 3 + 5 = 9
```

This is **exhaustive** (it spans every real 3×3 drift — dimension count) and **closed** (gl(3,ℝ) is a
Lie algebra; verified residual 3·10⁻¹⁶ over all 81 commutators) — a closure, not a catalogue. The
three structured non-drift axes (noise, nonlinearity, time-periodicity) and the composition operation
each close on their own named structures (below). Closure is **autonomous** — it needs no protecting
symmetry — so the meta-scale symmetry is a **substrate boundary condition** (strict-K3, route (b)),
not a structural output; its derived role is to suppress the O(κ) Sym₀ doublet-splitting channel so
the O(κ²) so(3) chiral seed leads. On a so-protected degenerate doublet the lift into a
counter-rotating meta-cycle is **forced**, and it is the same 2×2 normal form whose other branch is
the verified non-Hermitian exceptional point.

---

## Step 1 — the algebra (commutation relations)

The generators `character_primitives.py` actually deformed are, exactly, a basis of gl(3,ℝ):

| apparatus generator | algebra element | block |
|---|---|---|
| `damping` (`−(γ+s)I`) | `I` | center ℝ·I (1) |
| `chirality` mag+sign (`g·A_CYC`), `tilt`/orientation | `A_CYC = Lₓ+Lᵧ+L_z` (axial `(1,1,1)`) and the rest of so(3) | so(3) (3) |
| `splitting-detuning` (`SPLIT = E₁E₁ᵀ − E₂E₂ᵀ`) | symmetric-traceless | Sym₀ (5) |

(Verified: `A_CYC`'s axial vector is `(1,1,1)`, residual onto so(3) = 5·10⁻¹⁶; `SPLIT` lands in Sym₀,
residual 3·10⁻¹⁶.)

**Bracket table (Cartan grading), all verified numerically.** With 𝔨 = so(3) (compact) and 𝔭 = Sym₀:

```
[ℝ·I, · ] = 0          (the trace is central — damping commutes with everything)
[𝔨, 𝔨] ⊆ 𝔨            (so(3) closes — rotations compose to rotations)
[𝔨, 𝔭] ⊆ 𝔭            (a rotation of a symmetric-traceless tensor is symmetric-traceless)
[𝔭, 𝔭] ⊆ 𝔨            (two detunings commute to a rotation — the Cartan relation)
```

`[A,S]` of an antisymmetric `A` and symmetric `S` is symmetric (`(AS−SA)ᵀ = AS−SA`) and traceless,
hence in 𝔭; `[S₁,S₂]` is antisymmetric, hence in 𝔨 = so(3). This is the Cartan decomposition of
gl(3,ℝ) = ℝ·I ⊕ sl(3,ℝ), with sl(3,ℝ) = so(3) ⊕ Sym₀ its symmetric-space split. **Closure is a
theorem of the Lie structure, not a fit.**

---

## Step 2 — autonomous-symmetry test (the formal narrow path for route (a))

The structure constants in Step 1 were computed with **no symmetry constraint** — no C₃ projection, no
"commute with a group" condition. gl(3,ℝ) closes **unconditionally**. Therefore:

> **Closure does not require — and does not entail — the protecting symmetry.**

Route **(a)** (symmetry as a *structural output* of closure) is **abandoned, with zero guilt**. Route
**(b)** is banked, now derived: the protecting symmetry is a **substrate boundary condition**,
parameterized into the claim. Its role is precise and derived, not posited:

The bare collective block is `−γI₃` (triply degenerate: `A_CYC·(1,1,1)=0`, so the collective slow
modes carry no rotation). A symmetric (even-parity) inter-block coupling perturbs this doublet through
**two channels**: a direct **O(κ) Sym₀** splitting and a Schur-induced **O(κ²) so(3)** chiral seed
(`B D⁻¹ C`, the `√3·g/(γ²+3g²)` antisymmetry). Verified scaling on the collective doublet:

| coupling | doublet behaviour | leading channel | meta-cycle |
|---|---|---|---|
| C₃-covariant | complex pair, real-split ≈ 0 | ω_meta ~ κ^**1.94** (≈2: the so(3) seed) | **alive** |
| generic even-parity | real-axis split ~ κ^**1.00** (the Sym₀ channel) | O(κ) splitting | **killed** |

The protecting symmetry is exactly the condition that the substrate's coupling **commute with C₃**, so
its Sym₀ doublet-splitting component vanishes (the E-doublet is forbidden to split at O(κ)); only then
does the O(κ²) so(3) seed lead and the meta-cycle survive. **Strict-K3 posture:** "generic coupling
kills the cycle" is not a failure — it is the rigorous validation that the lift is a *forced
trajectory requiring exact conditions*, not a free lunch occurring everywhere.

---

## Step 3 — the law of the lift

On the 2-D collective doublet the residual deformation is a 2×2 normal form built from exactly the
two non-central channels (Sym₀ splitting `δ` and so(3) rotation `ω`):

```
M₂ = −γ′ I₂ + (δ/2)·Z + ω·J,     Z = diag(1,−1) [Sym₀],   J = [[0,−1],[1,0]] [so(2)]
eigenvalues = −γ′ ± √( (δ/2)² − ω² ).
```

- **Protected (symmetry on → δ = 0):** the only residual deformations on a *degenerate* doublet are
  damping `I₂` and rotation `J`; a real 2×2 antisymmetric block has eigenvalues `±iω`. So the lift is
  a **complex-conjugate pair → a counter-rotating meta-cycle, forced** (verified: `−1 ± i`).
- **δ = 2ω:** eigenvalue coalescence — the **exceptional point** (the tilt-death of Part 4).
- **δ > 2ω:** real split, rotation gone.

The protected lift and the EP death are **two branches of one normal form**. The complex branch
satisfies `ω_eff² = ω² − (δ/2)²` at slope −1, intercept ω², **R² = 1.0000** — identical to the
non-Hermitian EP verified in `establishment_compare.py` (`pa:nonhermitian-ep`). MPA adds the reading,
not the form.

---

## The complete deformation space (closure beyond the linear drift)

gl(3,ℝ) is the linear-drift core. The full deformation space of the (possibly time-dependent,
stochastic) character-bearing operator closes as the core **plus** three structured axes and one
composition — each landing on a named, closed structure, so the set is exhaustive for an SDE on ℝ³:

| axis | object | closed structure (prior-art) |
|---|---|---|
| linear drift | gl(3,ℝ), Cartan-graded | the bracket table above |
| noise / drive | diffusion tensor `Q ∈ Sym⁺(3)` | continuous Lyapunov (NESS covariance), `ness-currents` |
| nonlinearity | gain/saturation (self-field) | normal forms — pitchfork/Hopf, `bifurcation-normal-forms`, `frank-autocatalysis` |
| time-periodic | rotating parametric squeeze | Floquet/monodromy → Adler circle map, `adler-locking` |
| **composition** | inter-block coupling + Schur | coarse-graining coupled triads returns again `(gl(3) drift, Sym⁺ noise)` — the two-mode-kernel RG type-identity |

The composition row is the recursion closure: the deformation-algebra is **closed under
coarse-graining**, which is why the cascade re-renders the same character object one level up.

---

## Gate check (against the character-primitives battery spec — falsifier now in [`../framework/character_receipts_engine.md`](../framework/character_receipts_engine.md) §deformation-generators)

- **(C) closure — DERIVED.** gl(3,ℝ) Cartan decomposition: exhaustive (dim 9 = 1+3+5) and closed
  (residual 3·10⁻¹⁶). Extensions close on named structures. A closure, not a catalogue. ✓
- **(R) each response forced.** EP √-law (R²=1.0000), Arnold/Adler θ_c∝κ, pitchfork K_c=c/β=½,
  non-reciprocity √3g/(γ²+3g²), Floquet tongue — all on canonical forms with prior-art receipts. The
  ~39° symmetric-cone node and the non-uniform-squeeze secondary tongues are **model-specific → stay
  frontier, do not promote**. ✓ (non-model-specific cells)
- **(I5).** *Collapse* — over-determined: the basis is fixed three independent ways (dimension count,
  the bracket grading, and the apparatus generators landing in it at 10⁻¹⁶), not a single-register
  identity. *Iff-chain* — the basis is the **entailed** Cartan decomposition of gl(3,ℝ), not an
  asserted list (this is the load-bearing win over the table). *Flow* — every **response** moves with
  the operating point (EP threshold δ=2ω, ω_meta∝κ², Arnold θ_c∝κ all parametric); the Cartan
  structure constants are the algebra's invariants (Lie skeleton), not inert dynamical constants in a
  response, so flow is not tripped. ✓
- **(G) goalpost-optic.** The basis *shrinks* the falsifiable surface: every character deformation
  must be a gl(3,ℝ) element (or a named extension), and every response must hit its canonical form — a
  deformation that fails to decompose, or a response that misses its form, is then a clean kill. ✓
- **symmetry:** scoped **conditional** (route (b) / strict-K3), derived role characterized. ✓

---

## The conditional operator (Step 4 — drafted, for the next-move engine edit)

For `character_engine.md` as an `OPERATORS`-adjacent section "deformation generators":

> **Deformation generators (conditional).** The linear deformations of the character-bearing drift are
> gl(3,ℝ) = ℝ·I (damping) ⊕ so(3) (chirality mag+sign+orientation) ⊕ Sym₀ (splitting/detuning), Cartan-
> graded `[𝔨,𝔨]⊆𝔨, [𝔨,𝔭]⊆𝔭, [𝔭,𝔭]⊆𝔨`; with the noise (diffusion tensor, Lyapunov), nonlinear
> (normal-form), time-periodic (Floquet) extensions and composition (Schur) closing the space. **Given
> a substrate symmetry that protects the collective doublet against O(κ) Sym₀ splitting**, the closure
> forces the O(κ²) so(3) chiral seed to lift the degeneracy into a **protected counter-rotating
> meta-cycle** — the complex branch of the 2×2 normal form `−γ′ ± √((δ/2)²−ω²)` whose δ=2ω branch is
> the exceptional point. The symmetry is a substrate boundary condition (parameterized), not a
> structural output; generic even-parity coupling splits at O(κ) and kills the cycle.

---

## What stays frontier (do not promote)

The **~39° symmetric-cone chirality-reversal node** (model-specific — matched neither Berry 60° nor the
magic angle) and the **non-uniform-squeeze secondary-tongue structure**. These are the K2 cells; they
stay in `frustration-ascent` / `wall-as-type-boundary` as frontier, by design.

The **coverage/life claim** ("real substrates' — and the syn3 alive-loop's — character is a composition
of these") remains the parked instance frontier (`syn3_alive_loop_handoff.md`). This derivation is its
**foundation**, not a substitute: it earns the structural law syn3 would later land on.
