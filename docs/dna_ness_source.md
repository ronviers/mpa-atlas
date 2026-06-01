# DNA-NESS real instance — source & provenance (for the record)

The Gate-2 emergent-identity node's confirmed real substrate. All rate constants used in
`mpa-conform/scripts/emergent_identity_dna_ness.py` and `dna_ness_crosscheck.py` are **facts cited
from the paper's Supporting Information** (fair-use citation of measured values; the SI PDF itself
is not redistributed here — retrieve it via the open link below).

## Citation

James D. Nicholas, Erica Del Grosso, Andrew J. deMello, Josep Puigmartí-Luis, Francesco Ricci,
Alessandro Sorrenti — **"Sustained, reversible and adaptive non-equilibrium steady states of a
dissipative DNA-based system."** *Angewandte Chemie International Edition*, 2025.
DOI: [10.1002/anie.202512967](https://onlinelibrary.wiley.com/doi/10.1002/anie.202512967).

- Open preprint: ChemRxiv, DOI [10.26434/chemrxiv-2024-47pw9-v2](https://chemrxiv.org/engage/chemrxiv/article-details/681e0f6ae561f77ed4d2376b).
- Open SI (provided by the user as a legal access route):
  `https://chemrxiv.org/doi/suppl/10.26434/chemrxiv-2024-47pw9-v2/suppl_file/supporting_information_file.pdf`
  *(ChemRxiv bot-blocks programmatic download — 403; open in a browser.)*
- Open access via PMC: [PMC12535392](https://pmc.ncbi.nlm.nih.gov/articles/PMC12535392/).

## Which numbers came from where (SI Section 3, Tables S4/S5)

| symbol | value | units | SI location |
|---|---|---|---|
| `kdisp` | 6.61×10⁵ | M⁻¹s⁻¹ | Table S5, Exp. Fig. 2b (optimised) |
| `kdisp_r` | 5000 | M⁻¹s⁻¹ | Table S4 (fixed; gives `Kdisp≈100`) |
| `kOrebind` | 5×10⁸ | M⁻¹s⁻¹ | Table S4 |
| `kOrebind_r` | 1×10⁻⁶ | s⁻¹ | Table S4 |
| `kFrebind` | 5×10⁸ | M⁻¹s⁻¹ | Table S4 |
| `kFrebind_r` | 7.6×10⁻⁹ | s⁻¹ | Table S5 (set by detailed balance; we recompute = 7.56×10⁻⁹, matches) |
| `kcat` | 2.65 | s⁻¹ | Table S5, Exp. Fig. 2b |
| `kenz` | 3.2×10⁷ | M⁻¹s⁻¹ | Table S5, Exp. Fig. 2b |
| `kenz_r` | 0.1 | s⁻¹ | Table S4 |
| `[RNase H]` | 5.0×10⁻¹⁰ | M | Sec. 3 text |
| DNA duplex (Q_total) | ~50 | nM | Sec. 2/3 |

## Reaction network (SI Sec. 3.1 / Table S2), as we use it

Species: O (output), Q (quencher), OQ (output–quencher duplex), FQ (fuel–quencher heteroduplex),
F (RNA fuel), E (RNase H), FQE (enzyme–substrate), W (waste), EW (enzyme–waste), Ed (dead enzyme).

Core driven cycle (quencher's partner): `OQ →(fuel displaces output)→ FQ →(RNase-H hydrolysis)→ Q
→(output rebinds)→ OQ`, sustained by RNA-fuel hydrolysis; returns to equilibrium ~3 min after fuel
is cut (SI; our cross-check reproduces ~2.8 min). Our N=3 reduction tracks {OQ, FQ, Q} with the
enzyme folded to a pseudo-first-order drain; the full nonlinear network (with O, E, FQE explicit) is
in `dna_ness_crosscheck.py` and confirms the reduction (cycling-rate ratio 1.002).

## How it maps to the Gate-2 emergent-identity node

- **Two unprotected modules.** Module A = reversible DNA hybridization (the OQ–FQ–Q triangle),
  detailed-balanced **by the SI's own constraint** (𝒜=0). Module B = RNase-H hydrolysis (an acyclic
  FQ→Q drain, 𝒜=0 alone).
- **Minting.** Coupling (the enzyme acting on FQ) drives the pre-existing balanced cycle out of
  equilibrium → 𝒜≠0. The circulation is minted by the coupling; neither module carries it alone.
- **Protection.** sign(𝒜) is the discrete graph-flux bit, drive-locked by the irreversible enzyme;
  the affinity uses only measured constants ([F],[O] cancel around the cycle).
- **Sustained identity.** Cut the fuel/enzyme → 𝒜→0, circulation collapses (run-loop, observed
  experimentally) — not a stored state.
