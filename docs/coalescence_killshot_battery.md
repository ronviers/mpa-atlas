# Sign-Topological Killshot — the Interior-Circulation Battery

**Status: falsifier spec, partly runnable now (synthetic), kill/vindicate gated on
a real frustrated substrate. Not a boundary test.** Counterpart to
[`falsification battery.md`](falsification%20battery.md) (amplitude-seam
scaling-collapse). (Filename retains "coalescence": the exceptional point /
eigenvalue coalescence at 𝒜=0 is the boundary this battery deliberately **does not
visit** — the test is interior.) Canonical claims under test:
[`../framework/mpav1_compressed.md`](../framework/mpav1_compressed.md) §Central
commitment, §k_frust drain, §Two bits, §Asymptotic closure; receipts §Central
commitment, §846 (R1/R2/R3), §Homochirality. Trajectory and the three corrections
that shaped this scope: notes §12.

---

## 0. The principle — attach the math where character lives

Character *is* the holding against dissolution. At the boundary — chit→0, 𝒜=0,
trails→0 (all one boundary: the sign-erased critical surface / exceptional point /
asymptotic-closure limit, **never attained**) — there is no holding, so there is no
character to measure. Character is **degenerate at the boundary, rich in the
interior.** A falsifier that needs the boundary is malformed by the framework's own
structure. **Every test in this battery is a finite-operating-point measurement in
the open interval.** No NaNs, no zeros, no limit-cases.

The earlier "can-kill-can't-vindicate" framing was an artifact of formulating the
protection test as a flip-cost across the zero. The flip-floor is real but it is an
**entailed theorem**, not a measurement (§3). The decisive measurement is interior.

---

## 1. The object

The minimal carrier of gauge-irremovable circulation: a Harary triad △_H (directed
3-cycle, non-reciprocal, Harary-unbalanced), realised by the universal two-mode
kernel on an N=3 cycle.
- **Synthetic ruler:** `mpa-central/library/banach_frustrated.py` (linear N=3
  non-reciprocal OU; complex eigenpair, 𝒜 flat across a 20× noise sweep). It is the
  calibrated reference — built to carry the signature, so it cannot *kill* the
  central commitment, only stress-test internal consistency (§4 IK).
- **Real substrate (where the kill/vindicate lives):** the §Homochirality
  maintenance network, or a Harary-wired active metamaterial (Veenstra/Coulais/
  Bartolo rings). Bottleneck is the measurement protocol, not physics.

---

## 2. The invariant — the chimeric sign (not the triality)

The protected object is the **chimeric sign**: the cycle parity of the
Harary-unbalanced triad, the topological bit. It is **±1, gauge-irremovable,
intrinsically discrete at every finite D** ("no limit to approach"). It is the only
binary observable here — and the binary verdict is what makes this a killshot rather
than another graded measurement.

**Read the bit, not its shadows.** The k_frust *triality* — one topological excision
with three co-implied consequences (dynamical: complex Jacobian pair; thermodynamic:
Schnakenberg current J / affinity magnitude |𝒜|; info-geometric: homotopy
obstruction) — is the framework's **inferential fallback** for substrates where the
sign can't be read directly. Each consequence is a *graded, precision-threshold*
measurement (is |𝒜| flat to ε, is Im λ above noise) that re-imports the amplitude
baggage §0 exists to shed. Whacking the three consequences is not the test.

**The test (binary, interior):** the chimeric sign's **stability under finite
perturbation**. Vary drive/noise across a *finite range*; the sign either holds
(protected — topological bit) or flips/drifts (drive-set — amplitude bit in
disguise). sign(𝒜) is its drive-independent readout. No precision threshold, no
magnitude fit, no approach to zero — a ±1 verdict.

**Where the triality is still earned:** a real substrate that exposes only dynamics
(not its wiring) forces inference through the consequences. Use the triality there,
accept the graded reading. Where the substrate hands you the sign directly
(homochirality = a measured molecular handedness), read the bit.

---

## 3. The flip-floor is an entailed theorem, not a measurement

The ≥ln2 cost to flip the protected sign (§Two bits) **follows from** the signature
above; it is never measured by flipping. To flip the chirality the current must pass
through the sign-erased state (J→0), which is the erasure — Landauer gives ≥ln2 per
protected sign. So:
- the interior signature (§2) is the measurement;
- the flip-floor and "free to hold / costly to flip" are theorems entailed by it.

We do not visit the zero to establish protection. The structure that *forces* the
crossing-through-zero is read directly, in the interior.

---

## 4. KILL / VINDICATE conditions (all interior)

### Runnable now — synthetic internal-consistency falsifier (binary, could fail today)
`banach_frustrated.py` is built to carry the sign, so this tests the framework's own
consistency, not the central commitment. It is genuine — it *can* fire:
- **IK1 — chimeric sign not protected.** Vary drive/noise across a finite range at
  fixed wiring; if the chimeric sign (sign(𝒜)) **flips** without any rewiring → it
  was drive-set, not topological → the topological-bit claim is internally false.
  Binary: the sign flips or it doesn't.
- *(Corroborating, graded — the triality fallback, not the verdict):* whether |𝒜|
  stays flat while J scales, and whether the complex pair persists, across the same
  finite range. Reported, not relied on.

### The central commitment proper — needs a real frustrated substrate
- **RK1 — KILL.** A real substrate whose chimeric sign is **protected** (holds under
  finite drive variation, removable only by rewiring) with **no chimeric triad** in
  its coupling graph → central commitment dead.
- **RV1 — VINDICATE.** A protected chimeric sign, on real substrates, always sits on
  a chimeric triad. Homochirality is the named instance: the molecular handedness is
  the chimeric sign read directly; the test is whether it holds as drive varies over
  a finite range (not to zero).

---

## 5. What this is and is not

- It is a **well-formed, decisive, interior** test: it kills or vindicates the
  central commitment when run on a real substrate, with finite-operating-point
  measurements only.
- It is **not gated on a boundary.** The only gate is obtaining a real frustrated
  substrate to measure — the actual physics frontier (homochirality / metamaterial),
  not a limit-case standdown.
- The synthetic layer (IK1) is runnable now and can kill on internal inconsistency;
  a synthetic pass is calibration, not vindication.

---

## 6. Minimal apparatus

Extend `banach_frustrated.py` (do not rebuild):
1. Finite drive/noise sweep at fixed wiring; record the **binary chimeric sign**
   (sign(𝒜)) at each operating point; the verdict is whether it ever flips without
   rewiring (IK1). Drive stays finite throughout — never approaches zero.
2. Report |𝒜|, J, spec(M) alongside as the graded triality corroboration — logged,
   not the verdict.
3. ρ never clipped (asymptotic-closure; an attained 0/1 is a NaN tripwire). The
   deliverable is the ±1 sign-stability verdict, not a fitted quantity. PNG →
   `mpa-central/library/output/diagnostics/`.

The real-substrate measurement (RK1/RV1) reads the chimeric sign directly where the
substrate exposes it (homochirality: the handedness), and falls back to the triality
(cyclic fluxes + linearised-maintenance Jacobian spectrum) only where the wiring is
not directly inspectable.

---

## 7. What this measures

Whether the **chimeric sign** — the binary topological bit — is *protected* (holds
under finite perturbation) and whether a protected sign requires a chimeric triad,
**measured where character is rich**. The triality (current, affinity magnitude,
spectrum) is the inferential fallback, not the verdict; the flip-cost protection
follows as a theorem. Nothing in the test approaches the zero where character dies.
