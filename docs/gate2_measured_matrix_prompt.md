# Gate-2: request for a PUBLISHED, MEASURED rate matrix (third ask)

> **For the outbound research channel.** The first two asks returned the right *class*
> (finite-D stochastic-thermodynamic Markov networks) but the candidates were **synthetic
> constructions with hand-set rate parameters** — calibration, not a real instance. We already
> have those (`emergent_identity.py`, `emergent_identity_n4.py`, both pass). **We do not need
> another model. We need DATA.** This ask is deliberately narrow.

## The ask (one thing)

**One PUBLISHED, MEASURED rate matrix** — or a fully-specified kinetic scheme with *numerical*
rate constants from which we can assemble the generator — from **either**:

1. an **engineered kinetic-proofreading DNA strand-displacement network** (e.g. Mukherjee et al.,
   *JACS* 2024, the `J_ss = j_c1 + j_c2` two-emergent-cycle system), **or**
2. a **real allosteric enzyme** operating as a driven cycle (a measured kinetic scheme with rate
   constants — e.g. a motor ATPase, a GTPase cycle, a kinase with a measured 4-state scheme).

## Required — all four, or it is not what we need

- **(a) Explicit numerical rates.** Every transition rate `k_ij` (with units and the experimental
  conditions / fuel concentration that set them), enough to build the `N×N` generator. Point to the
  **specific table / figure / SI** that contains the numbers — not a qualitative scheme.
- **(b) A two-module decomposition** (or enough of the network that *we* can identify one): two
  individually-**unprotected** modules — each detailed-balanced / acyclic (`𝒜 = 0`) on its own —
  whose **coupling** closes the frustrated cycle. (For proofreading: the right- vs wrong-substrate
  recognition branches, or substrate-binding vs the fuel-driven step.)
- **(c) The drive, named physically** (ATP / GTP / RNA-fuel / Δμ): what "remove the drive" means
  (fuel → 0 ⇒ detailed balance restored, `𝒜 → 0`), and what "remove the coupling" means (which
  transition / strand to delete to break the cycle).
- **(d) Confirmation it is REAL** — measured, or engineered-and-characterized — with the citation
  (DOI) and the exact location of the rate constants (table / figure / SI).

## Deliverable

A numerical `N×N` generator (or an edge-list of rates) **ready to paste into
`emergent_identity.py`**, plus the source (DOI + table/figure/SI location) and the (b)/(c)
annotations. We run it through the protocol ourselves.

## Do NOT return

- **Another synthetic model with hand-set parameters** (`α, β, k=1, ΔE=…`). We have those; they are
  calibration, not a discharge.
- A qualitative analogy, or a scheme without numerical rate constants.
- Anything **Chern / EP / band-topological / lattice / physical-rotation** (excluded — see the prior
  screen).
- A model's **self-run "verdict."** We instance the numbers ourselves; the gate is discharged by
  running the matrix, never by citation or by a self-reported PASS. (The last return's protocol
  hardcoded its run-loop and exclusion tests to PASS and mis-stated its own affinity — do not repeat.)

## If the data is incomplete

Say so plainly and identify the **closest**: which rates are published, which are missing, and
whether an SI or a follow-up paper fills the gap. A precise *"here is what's available and what's
missing"* is far more useful than a fabricated or back-filled matrix. **Do not invent rate
constants** to complete a matrix — a partial real scheme with the gaps named beats a complete fake.

---

## Reconnaissance already done (2026-06-01) — fill THESE specific gaps

Both named leads were verified real + open-access, but **neither is turnkey**, and they fail
differently. The channel's job is to close the named gap, not to re-find the papers.

- **Kinetic proofreading** — Mukherjee, Sengar, Cabello-García, Ouldridge, *JACS* 2024,
  [10.1021/jacs.3c14673](https://pubs.acs.org/doi/10.1021/jacs.3c14673) (open: PMC11258683).
  Rate constants exist but are **scattered across SI Tables S9/S10/S11 + fitted figures** (9.3 MB
  SI, ODE-fit via Mathematica `ParametricNDSolve`). Structure: a Hopfield **template cycle**
  `T → ML/T → MT → T` — a **single driven cycle by design**, *not* two-unprotected-modules-coupled
  ⇒ **near-miss on MINTING** (clean on protection + run-loop: drop the proofreader ⇒ detailed
  balance returns, Fig S54). *Gap to fill:* extract the SI rates into a generator, and give an
  honest call on whether template-binding vs proofreader-removal can be cast as two individually-
  unprotected modules — or concede it is a designed cycle (instances protection + run-loop, not
  minting).
- **DNA-NESS** — Nicholas et al., *Angew. Chem. Int. Ed.* 2025,
  [10.1002/anie.202512967](https://onlinelibrary.wiley.com/doi/10.1002/anie.202512967)
  (open: PMC12535392 / ChemRxiv). Real dissipative cycle (`OQ + F → O + FQ` strand displacement →
  enzymatic hydrolysis of `FQ` → regenerates `OQ`), driven by **RNA fuel**, **returns to
  equilibrium ~3 min after fuel is cut** (clean run-loop). Rates in **SI Tables S4/S5** (only
  `k_disp = 5.7×10⁵ M⁻¹s⁻¹` in the main text). BUT it is a **nonlinear chemical reaction network**
  (bimolecular mass-action), *not* a linear Markov generator — reducing to our `N×N` generator
  needs a modeling choice (pseudo-first-order rates at a fixed fuel concentration / CTMC reduction
  around the NESS). *Gap to fill:* the discrete-state reduction — which pseudo-first-order rates,
  at what fuel concentration — so it becomes a linear generator, plus the two-module split
  (strand-displacement module vs enzymatic-hydrolysis module, coupled at the shared `FQ` species).

Either gap, closed with **real SI numbers** (not invented), gives the first runnable real instance.
