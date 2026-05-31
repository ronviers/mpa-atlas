# Vocabulary refactor spec — retiring "violation" and "wall" as prose anchors (2026-05-31)

**Why.** "violation" and "wall" are *prose attractors*: once they are the load-bearing nouns, any AI rewrite
of the public-facing engine anchors its register to them — "violation" → transgression/legalism, "wall" →
barrier/platformer/"hitting a wall" — and the downstream prose goes cringe. The fix is **better concept-names,
not synonyms** (a synonym re-anchors the same way). This spec lays the track for the eventual full engine
rewrite (a multistep process); it is NOT that rewrite. Step 1 (this doc + the prose rename) clears the two
worst anchors so the rewrite can breathe.

**Discipline.** Live canonical only. `framework/archive/**` is untouched — git history holds the past
(`feedback_forward_only_no_lineage`). Coined-name preference honored (`feedback_prefer_coined_names`).

---

## "violation" → the FD *ratio* / FDR *departure* (Ron's choice; recommended)

**Diagnosis.** Half-inherited from the literature — Harada–Sasa's result is literally titled "violation of
the FDT," which is why it crept in. It names two things:
- **the factor X** (Cugliandolo–Kurchan): $X=1$ at equilibrium, $X<1$ away. → rename to the established
  neutral term **the fluctuation–dissipation ratio** $X$ (this is CK's own word, not a coinage). "violation
  factor" → "FD ratio."
- **∫FDR-violation $=\langle\sigma\rangle$**: the departure of fluctuation-from-response that equals the
  dissipation. → **FDR departure** (neutral, measurement-register).

**Register payoff:** "violation" sounds like enforcement; "ratio / departure" sounds like *measurement* —
which is what MPA *is* ("a measurement discipline," engine header). Note in the rewrite: cite that the
literature says "violation"; MPA reads it as a ratio/departure (imports-and-metabolizes — name the source).

### Live instances (old → new)
| file | old | new |
|---|---|---|
| `mpa_engine.md` L119 | "violation factor $X$" | "fluctuation–dissipation ratio $X$" |
| `mpa_engine.md` L179, L188 (×2), L202 | "$\int$FDR-violation" | "$\int$FDR-departure" |
| `mpa_engine.md` L188 | "the violation factor running through…" | "the FD ratio running through…" |
| `mpa_fdr_treatment.md` L12 | "external-frame violation factor" | "external-frame FD ratio" |
| `mpa_fdr_treatment.md` L19 | "self-frame violation factor" | "self-frame FD ratio" |
| `mpa_fdr_treatment.md` L21 | "integrated external FDR-violation" | "integrated external FDR-departure" |
| `mpa_fdr_treatment.md` L41, L62, L64, L68 | "FDR-violation (identity/is the dissipation/and precision-cost)" | "FDR-departure …" |
| `mpa_fdr_treatment.md` L47 | "inserts a violation factor $X$" | "inserts a fluctuation–dissipation ratio $X$" |
| `mpa_receipts_engine.md` (FDR-violation mentions) | "FDR-violation" | "FDR-departure" |
| `mpa_frontier.md` (FDR-violation mentions) | "FDR-violation" | "FDR-departure" |
| `mpa_prior_art.md` (`harada-sasa` gloss) | keep "violation" ONCE as the literature's term, in quotes | — |

**Keep one literal "violation"**: in the `pa:harada-sasa` prior-art gloss, as `"violation of the FDT"` in
quotes — that IS the imported result's name; deleting it hides the provenance. Everywhere else → ratio/departure.

---

## "wall" → disambiguate THREE meanings, then rename (Ron's choice for the main one: marginal point / ε=1 locus)

**Diagnosis.** "wall" is overloaded across THREE distinct physics objects in live canon — a blind swap would
conflate them. Plus it appears in stable KEYS (handled separately below).

1. **The ε≥1 compression-divergence point** (the main one; engine COMPRESSION, frontier, receipts). The tower
   stops contracting ($\varepsilon=\lVert\mathcal{C}\rVert\ge1$), $\Phi_{\text{total}}$ diverges, the plateau
   loses normal hyperbolicity. → **the marginal point / the $\varepsilon=1$ locus** (Ron's choice). It is the
   marginal eigenvalue of the RG flow (loss of normal hyperbolicity) — physics-formal, reads as a critical
   point, zero platformer connotation. "the Wall" → "the marginal point ($\varepsilon=1$)"; "past the Wall" →
   "past marginal ($\varepsilon>1$)"; "at the Wall" → "at the $\varepsilon=1$ locus."
2. **The capacity hard-cutoff** (engine CAPACITY, Erlang-B: "hard-wall substrate," "$\sqrt D$ ceiling"). This
   is a DIFFERENT object — a hard occupancy cutoff, not the RG marginal point. → keep **"hard cutoff" /
   "ceiling"** (already uses "ceiling" alongside). "hard-wall substrate" → "hard-cutoff substrate";
   "Capacity wall" (falsifier name) → "Capacity ceiling."
3. **The "dt wall" in units** (`mpa_units.md` L58, integrator timestep bound). → "the dt **bound**" / "the
   stiffness bound." Trivial, prose-only.

### Live instances (old → new) — PROSE
| file | old | new |
|---|---|---|
| `mpa_engine.md` L25 | "$\varepsilon\ge1$ = Wall" | "$\varepsilon\ge1$ = the marginal point" |
| `mpa_engine.md` L161 | "Dynamic conjugate (same wall)" | "(same ceiling)" |
| `mpa_engine.md` L164 | "hard-wall substrate" (×2) | "hard-cutoff substrate" |
| `mpa_engine.md` L168 (heading) | "COMPRESSION / WALL" | "COMPRESSION / THE MARGINAL POINT" |
| `mpa_engine.md` L173 | "**WALL** ($\varepsilon\ge1$)" | "**MARGINAL POINT** ($\varepsilon\ge1$)" |
| `mpa_engine.md` L175 | "Wall = loss of normal hyperbolicity"; "Post-Wall" | "The marginal point = loss of normal hyperbolicity"; "Past marginal" |
| `mpa_engine.md` L228 | "$\varepsilon\to1$@Wall" | "$\varepsilon\to1$@marginal" |
| `mpa_engine.md` L291 | "Capacity wall"; "hard-wall" | "Capacity ceiling"; "hard-cutoff" |
| `mpa_engine.md` L296 | "Wall closure-loss"; "at the Wall"; "Post-Wall" | "Marginal closure-loss"; "at the marginal point"; "Past marginal" |
| `mpa_engine.md` L297 | "near the Wall" | "near the marginal point" |
| `mpa_units.md` L58 | "the dt wall" | "the dt bound" |
| `mpa_frontier.md` / `mpa_receipts_engine.md` | prose "Wall" (NON-key) | "marginal point" (per context) |

### KEYS — DO NOT rename this session (stable identifiers, cross-ref'd under bridge-invariant I1)
These read as identifiers in backticks, NOT prose, so they do **not** re-anchor a rewrite. Renaming them
requires synchronized frontier↔receipts↔engine surgery (I1: every `staked` ↔ one frontier entry) — a later
sequenced step, not worth breaking I1 under time pressure:
- `wall-as-type-boundary` (frontier key) — **keep**
- `battery:wall-ladder` (frontier key) — **keep**
- receipts `§Wall — chaos mechanism` (receipt key) — **keep the key**; its prose body renames "Wall" → "marginal point"
- engine `Wall = loss of normal hyperbolicity` as a *named claim handle* — rename prose; if any doc cross-refs
  the literal string, leave a one-line alias note (none found in this pass).

(When the full rewrite runs, the keys rename in one synchronized pass with an I1 re-audit. Logged for that step.)

---

## EXECUTION LOG (step 1, done 2026-05-31)

Renamed **prose** in the live set: `mpa_engine.md` (all 10 "wall" + 5 "violation" → marginal point / ceiling /
hard-cutoff / FD ratio / FDR-departure), `mpa_fdr_treatment.md` (8 "violation" → FD ratio / FDR-departure),
`mpa_units.md` (2 "wall" → bound), `mpa_receipts_engine.md` (2 FDR-violation → FDR-departure). Engine verified
clean of both anchors (one residual was a Tier-B line authored earlier this session — fixed).

**Deliberately NOT renamed (scope discipline):**
- **Frontier/receipts "Wall" prose** — nearly all sits *inside* the `wall-as-type-boundary` / `battery:wall-ladder`
  / `§Wall — chaos mechanism` key entries; renaming the prose while keeping the keys creates internal
  dissonance ("the `wall-as-type-boundary` entry … near the marginal point"). These move in **step 2** (the
  synchronized key-rename, keys + their prose together, with an I1 re-audit). The frontier/receipts are the
  *internal ledger*, not the public-facing rewrite target, so the cringe-anchor risk is low there.
- **"TUR violation"** (frontier `battery:dimensionless-self-probe`) — standard physics ("violates the TUR
  bound"), NOT the FDR-departure anchor. Left.
- **"Both violations are the pre-excluded illegitimate maps"** (frontier `scale-covariant-circulation`) —
  generic usage, not the anchor. Left.
- **`pa:harada-sasa` literal "violation of the FDT"** — keep as the imported result's name (provenance).

## Sequence for the eventual full rewrite (this is step 1)
1. **[this session]** spec + prose rename of the two anchors (ratio/departure; marginal point/ceiling/bound).
2. retire the stable keys in one synchronized frontier↔receipts↔engine pass (I1 re-audit).
3. a second anchor-sweep for any *other* register-cringe terms a fresh read surfaces (candidates noticed:
   "killshot," "tripwire," "fraying" — evaluate, don't presume).
4. the public-facing engine rewrite proper — compelling prose, telos preamble (the parked alive-loop why),
   asterisked. NOT in a tool-colored session.
