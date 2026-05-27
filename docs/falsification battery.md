# Finite-Drive Seam-Width Falsification Battery

## (Scaling-Collapse Version — operational draft)

This battery is designed to answer one question cleanly:

> Does the survivability seam behave like a genuine universal crossover structure, or is the apparent “soft seam” merely a fitted artifact?

The target invariant is **not** a coefficient series.

The target invariant is:

[
(\alpha,F)
]

where:

* (\alpha) = seam-width exponent
* (F(z)) = universal crossover profile

with scaling coordinate:

z=\frac{\gamma-D}{w(D)},\quad w(D)\sim D^{-\alpha}

---

# 0. Core claim under test

The framework predicts:

1. finite-(D) seams are soft,
2. seam width shrinks systematically with drive,
3. crossover curves collapse onto a universal profile,
4. the profile is substrate-independent *within a universality class*,
5. Boolean logic is the (w(D)\to0) limit.

Failure of collapse falsifies the strong crossover claim.

---

# 1. Minimal apparatus

You need:

* a control parameter (\gamma),
* a drive/stiffness parameter (D),
* a binary or quasi-binary survivability observable.

Natural observable:

[
P_{\mathrm{survive}}(\gamma,D)
]

or equivalently:

[
\Delta_C(\gamma,D)
]

interpreted as:

* merge success probability,
* stable coexistence fraction,
* persistence indicator,
* logical survivability rate.

---

# 2. Required data structure

For each fixed (D_i):

1. sweep (\gamma) across threshold,
2. record transition curve,
3. repeat for many (D_i).

Minimum useful grid:

* 8–12 values of (D),
* 50–200 samples along (\gamma),
* multiple stochastic repeats per point.

---

# 3. Raw falsifier (before any fitting)

Plot raw curves:

[
P(\gamma,D_i)
]

against:

[
\gamma-D_i
]

If curves sharpen with increasing (D), proceed.

If they:

* wander irregularly,
* broaden inconsistently,
* bifurcate unpredictably,

then the seam-width hypothesis is already damaged.

---

# 4. Width extraction test

Define seam width operationally.

Recommended:
full-width between:

* (P=0.25),
* (P=0.75).

Call this:

[
w(D)
]

Then fit:

w(D)\sim D^{-\alpha}

Extract:

* exponent (\alpha),
* confidence interval,
* goodness-of-fit.

---

# 5. Primary falsifier — scaling collapse

Rescale curves using:

z=\frac{\gamma-D}{w(D)}

Then replot:

[
P(\gamma,D)\to P(z)
]

The strong claim predicts:

[
P(\gamma,D)\approx F(z)
]

for *all* sufficiently large (D).

---

# PASS condition

All curves collapse onto one profile:

* same shape,
* same tails,
* same transition width,
* independent of (D).

---

# FAIL conditions

Any of:

* profile changes with (D),
* skew drifts,
* tails change class,
* width law unstable,
* no single (\alpha),
* multiple incompatible collapse families.

This falsifies universal seam scaling.

---

# 6. Universality-class discrimination

Fit collapsed curve against candidate families:

## Gaussian / diffusive

F(z)=\frac12\left(1+\operatorname{erf}(z)\right)

Predicts:

* additive noise,
* central-limit scaling,
* usually (\alpha=\tfrac12).

---

## Logistic

F(z)=\frac1{1+e^{-z}}

Predicts:

* multiplicative threshold competition,
* mean-field activation structure.

---

## Stretched / skewed crossover

Heavy-tail or asymmetry class.

Evidence for:

* correlated fluctuations,
* aging,
* glassy memory,
* non-Markovian structure.

---

# 7. The hard-seam falsifier

This is extremely important.

Test whether width actually vanishes.

Compute:

[
\lim_{D\to\infty} w(D)
]

If:

* width saturates,
* asymptotes to finite constant,
* oscillates,
* or bottoms out,

then:

* the Boolean sharp-threshold limit fails,
* asymptotic closure is damaged,
* seams are intrinsically soft rather than finite-drive-softened.

That is a major falsifier.

---

# 8. The orthogonal-seam test (critical)

You already identified two distinct seam manifolds:

## Drive seam

[
\gamma\approx D
]

## Switching seam

[
\gamma\approx0
]

Do NOT conflate them.

Run collapse independently on:

* threshold-survival seam,
* switching/bifurcation seam.

Possible outcome:

* one collapses,
* the other does not.

That is scientifically valuable.

---

# 9. Noise-spectrum falsifier

The framework increasingly suggests:

* seam width is fluctuation-controlled.

So vary noise model independently.

Compare:

* additive Gaussian,
* multiplicative,
* correlated,
* colored,
* heavy-tail.

If universality survives:
strong evidence.

If profile/exponent changes completely:
then seam structure is not universal but noise-model-specific.

---

# 10. FDR linkage test (advanced)

If you can measure:

* dissipation,
* fluctuation spectra,
* aging slopes,
* or effective temperature,

test whether:

[
w(D)\propto \sigma_{\mathrm{eff}}(D)
]

If seam width tracks FDR violation scale:
that strongly supports the Character-wing interpretation.

If completely decoupled:
the FDR bridge weakens.

---

# 11. Strongest possible falsifier

This is the kill shot.

Find two substrates with:

* same measured (w(D)),
* same (\alpha),

but:

* incompatible collapse profiles.

Or:
same profile class but incompatible exponents.

That destroys universality-class interpretation.

---

# 12. Interpretation guide

## Best-case outcome

You recover:

* stable (\alpha),
* universal collapse,
* substrate-family profile classes,
* predictable seam sharpening.

Then the framework has identified a genuine crossover structure.

---

## Medium outcome

Collapse exists only within substrate families.

Then:
MPA becomes a taxonomy of crossover classes rather than one universal seam law.

Still strong.

---

## Weak outcome

No stable collapse.
Exponent unstable.
Profile drifts arbitrarily.

Then:
the “soft seam” is probably a fitted artifact rather than a structural invariant.

That would seriously damage the deformation narrative.

---

# 13. Important discipline rule

Do NOT overfit.

You already identified the danger correctly.

The invariant is not:

* “can we fit a curve?”

The invariant is:

* scaling collapse with minimal free structure.

If a new parameter is needed for every (D),
the theory is not compressing reality.

Reality is compressing the theory.

---

# 14. What this battery actually measures

Not logic.

Not truth.

Not algebra directly.

It measures:

> how sharply a driven dissipative system can operationally distinguish survivable from nonsurvivable structure.

That is a physically meaningful object.

And mathematically it lives closest to:

* finite-size scaling,
* crossover theory,
* boundary layers,
* RG universality,
* nonequilibrium criticality.
