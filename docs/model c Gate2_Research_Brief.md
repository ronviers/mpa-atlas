# Gate-2 Substrate Re-Screen — Research Brief
## Emergent-Identity Instance (Sharpened Prompt)
**Date:** 2026-06-01
**For:** Outbound research channel
**Supersedes:** Broad "chiral substrate" hunt

---

## Executive Summary

The Gate-2 screen has been **discharged by one primary candidate** and **partially satisfied by four experimental directions**. The decisive discriminator — protection as the **discrete broken-detailed-balance affinity sign**, not band-topology or exceptional-point — has been successfully applied.

**Primary Qualified Candidate:**
- **Allosterically-coupled two-state subsystems (N=4)** — a finite-dimensional chemical reaction network where coupling two individually detailed-balanced 2-state systems mints a frustrated 4-cycle with sign-protected circulation. The cycle affinity is `A = 2·ln(β/α)`, where α and β are allosteric coupling factors. Energy biases and rate magnitudes completely cancel; sign(A) reverses only by rewiring the allosteric asymmetry.

**Closest Experimental Analogs:**
1. DNA strand displacement NESS systems (continuous fuel, ~4-5 states)
2. De novo kinetic proofreading DNA networks (JACS 2024, emergent cycles)
3. Enzyme kinetic asymmetry models (4-state directional cycles)
4. Shear-driven 3-state metastability (probability current pinning)

---

## The Screen (Recap)

### What we are looking for
A **real** driven-dissipative substrate in which **coupling two individually-unprotected subsystems mints a sustained protected circulation** that neither had — and whose protection is the **discrete broken-detailed-balance affinity sign**, in a **finite-dimensional** system.

### Three falsifiable components
1. **Minting:** Each subsystem alone has `A = 0` (detailed balance, no frustrated cycle). Coupled, the union has `A ≠ 0`, `J ≠ 0`.
2. **Protection = discrete graph-flux sign:** `sign(A)` survives reciprocal/gradient deformations; reverses only by rewiring.
3. **Sustained identity:** Bit exists iff both drive and coupling are maintained. No latch, no storage.

### Hard Exclusions
- ❌ Chern/band-topological protection
- ❌ EP-as-protection
- ❌ Physical/spatial rotation
- ❌ Lattice/thermodynamic-limit requirements

---

## Primary Candidate: Allosteric Coupling of Two 2-State Subsystems

### State Space
States are pairs `(A_i, B_j)` where `i,j ∈ {0,1}`:
- `0 = (A=0, B=0)`
- `1 = (A=1, B=0)`
- `2 = (A=1, B=1)`
- `3 = (A=0, B=1)`

### Graph Structure
```
      0 ──A──► 1
      ▲        │
      │B       │B
      │        ▼
      3 ◄──A── 2
```
The 4-cycle `0 → 1 → 2 → 3 → 0` is the emergent frustrated cycle.

### Subsystems (Decoupled)
- **Subsystem A:** Two independent 2-state equilibria `(0↔1)` and `(2↔3)`. Each detailed-balanced. No cycle → `A_A = 0`.
- **Subsystem B:** Two independent 2-state equilibria `(0↔3)` and `(1↔2)`. Each detailed-balanced. No cycle → `A_B = 0`.

### Coupling (Allosteric)
The rate of A's transition depends on B's state:
- `k_A^f(B=0) = k_A exp(-ΔE_A/2)`
- `k_A^f(B=1) = k_A exp(-ΔE_A/2) · α` (allosteric enhancement)
- `k_A^r(B=1) = k_A exp(+ΔE_A/2) / α` (reciprocal suppression)

The rate of B's transition depends on A's state:
- `k_B^f(A=0) = k_B exp(-ΔE_B/2)`
- `k_B^f(A=1) = k_B exp(-ΔE_B/2) · β` (allosteric enhancement)
- `k_B^r(A=1) = k_B exp(+ΔE_B/2) / β` (reciprocal suppression)

### Rate Matrix W (column-stochastic generator)
```
        j=0           j=1           j=2           j=3
i=0  -(kA0+kB0)     kA_r(B=0)     0             kB_r(A=0)
i=1   kA_f(B=0)    -(kAr+kBf1)    kB_r(A=1)     0
i=2   0             kB_f(A=1)    -(kBr1+kAf1)   kA_r(B=1)
i=3   kB_f(A=0)     0             kA_f(B=1)    -(kAr1+kBr0)
```

### Numerical Example
Parameters: `k_A=1, k_B=1, ΔE_A=1, ΔE_B=0.5, α=2, β=1.5`
```
W = [[-1.3853,  1.6487,  0.0000,  1.2840],
     [ 0.6065, -2.8169,  0.8560,  0.0000],
     [ 0.0000,  1.1682, -2.0691,  0.8244],
     [ 0.7788,  0.0000,  1.2131, -2.1084]]
```

### Cycle Affinity
**Analytical:** `A = 2·ln(β/α)`
- Energy biases `(ΔE_A, ΔE_B)` **completely cancel** in the cycle product
- Rate magnitudes `(k_A, k_B)` **completely cancel**
- `sign(A) = sign(ln(β/α)) = sign(β - α)` for positive rates
- **Protection:** sign(A) is invariant under reciprocal deformations (scaling forward+reverse rates together, changing energy barriers)
- **Reversal:** sign(A) flips only by rewiring (changing α/β, i.e., changing the allosteric coupling topology or drive polarity)

### Steady-State Current
`J = 0.01105` (non-zero, sustained NESS circulation)

### Run-Loop Tests
- **Kill drive** (α=β=1): `A → 0`, `J → 0`
- **Kill coupling** (make rates independent of partner state): `A → 0`, `J → 0`
- **No latch, no storage** — bit is a run-loop

### Hard Exclusions Check
- ✅ Finite-D: `N=4`
- ✅ No lattice: discrete state space, no spatial structure
- ✅ No EP: real spectrum, min eigenvalue gap = 0.696
- ✅ No Chern: no band topology
- ✅ No physical rotation: internal state-space circulation

---

## Protocol Verification

The candidate has been instanced through `emergent_identity.py`:

```
[TEST 1: MINTING]           PASS
[TEST 2: PROTECTION]        PASS  (sign stable under 100 reciprocal deformations)
[TEST 3: RUN-LOOP]          PASS  (kill drive/coupling → collapse)
[TEST 4: HARD EXCLUSIONS]   PASS

FINAL VERDICT: GATE DISCHARGED — CANDIDATE QUALIFIES
```

---

## Experimental Direction: DNA Strand Displacement Networks

The closest experimental realization of the Gate-2 pattern is in **DNA strand displacement chemistry**:

### Sustained NESS DNA Systems (2024)
- **System:** Continuous RNA fuel infusion maintains a dissipative strand displacement cycle
- **States:** OQ, O, F, FQ, Q (~4-5 species states)
- **Drive:** Fuel hydrolysis (analogous to ATP in biological systems)
- **NESS:** Confirmed by fitting model to experimental data; system equilibrates when fuel is cut off
- **Reference:** PMC12535392 / ChemRxiv 2024

### Kinetic Proofreading DNA Networks (JACS 2024)
- **System:** De novo engineered Hopfield-style kinetic proofreading in DNA strand displacement
- **States:** Template T, monomer-bound ML/T, MT, proofreader P, product MN
- **Emergent cycles:** Two coupled recognition cycles (right vs wrong monomer) with shared template
- **Key quote:** "overall steady state flux is acquired as the sum of fluxes of two emergent cycles, J_ss = j_c1 + j_c2"
- **Reference:** Mukherjee et al., JACS 2024

### Mapping to Gate-2
These systems satisfy:
- ✅ Finite-D chemical network
- ✅ NESS maintained by fuel
- ✅ Internal circulation in species space
- ✅ No band topology, no EP

They need explicit decomposition into:
- Two unprotected subsystems (each with `A=0`)
- A coupling mechanism that mints the frustrated cycle
- Verification that the cycle affinity is sign-protected

**Recommended next step:** Design a 4-state DNA strand displacement network that explicitly implements the allosteric coupling model (Candidate 1). Each "subsystem" would be a 2-state toehold exchange reaction; the "coupling" would be implemented by a shared strand whose binding state modulates the rates of both reactions.

---

## Additional Theoretical Candidates

### 3-State Frustrated Cycle (Minimal)
- Two 2-state subsystems + coupling transition → 3-cycle
- Affinity: `A = 4·ln(γ) - (ΔE_A + ΔE_B)`
- Less clean protection (energy biases don't fully cancel)
- Verdict: Satisfies criteria but less robust than 4-state model

### Enzyme Kinetic Asymmetry (4-State)
- States: E, E_L, E_L*, E*
- Cycle: E → E_L → E_L* → E* → E
- Directionality set by kinetic asymmetry `q = ω/ω*`
- Verdict: Single cycle, not emergent from coupling. Adaptable by splitting into two 2-state conformational subsystems.

### Shear-Driven Metastability (3-State)
- States: A, B, C with direct and indirect paths
- Non-conservative force breaks microscopic reversibility
- Net cycle emerges from pinned probability currents
- Verdict: Close to Gate-2 structure. Could be mapped to 3-state candidate.

---

## Rejected Leads (Recorded)

| Lead | Reason for Rejection |
|------|---------------------|
| Topological insulator lasers (Harari/Bandres/Segev, Science 2018) | Chern-protected edge mode; protection is integer band invariant, not affinity sign |
| Bacterial vortex lattices | Physical rotation, not internal state-space circulation |
| Floquet-topological systems | Band-topological protection |
| EP-encircling systems | Protection located at exceptional point |

---

## What to Return (Per Candidate)

For each candidate, the gate is discharged by **instancing through the protocol**, never by citation.

**Required for full qualification:**
(a) Explicit coupling / rate matrix (ready for `emergent_identity.py`)
(b) Evidence parts are unprotected and union is frustrated (`A`, `J`)
(c) Whether protection is reciprocal-deformation-robust (vs Chern/EP)
(d) Whether killing drive collapses circulation (run-loop test)

**Candidate 1 provides all four.**

---

## Next Steps

1. **Experimental design:** Engineer a 4-state DNA strand displacement network implementing the allosteric coupling model. Use two toehold-exchange reactions as subsystems, coupled by a shared modulator strand.
2. **Parameter sweep:** Run `emergent_identity.py` over wide parameter ranges to map the robustness region.
3. **Physical instantiation:** Identify allosteric enzymes or synthetic molecular switches that can be configured as two coupled 2-state systems.
4. **Higher-order candidates:** Search for systems where two driven cycles couple to close a third frustrated cycle (N=6-8).

---

## Files

- `emergent_identity.py` — Gate-2 screening protocol (Python)
- This research brief — comprehensive candidate analysis
