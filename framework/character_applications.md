# Character — APPLICATIONS (downstream uses register)

**Purpose.** Capture downstream applications of the framework — rendering, pedagogy, specific substrate workings, simulation protocols, implementations, presentations, computational notebooks — without contaminating the core's epistemic register. `character_frontier.md` tracks the framework's *development* (proven / owed / staked / exploratory); this doc tracks the framework's *uses*.

**Load-bearing rule (anti-drift).** Entries here **USE** the core; they do not **EXTEND** it. Any entry that would assert a new structural claim, propose a new falsifier or kill condition, or redefine a coined object belongs in `character_frontier.md` (steeping rung initially) or in `character_engine.md` (via the frontier promotion gates), **not here**. This rule is algorithmic — every proposed entry must pass the five ANTI-DRIFT checks below before being added.

**This doc is self-describing.** Future authors (human or AI) read this doc cold, then apply the AUTHORING PROCEDURE to add items. No external context required.

---

## SCHEMA — mandatory fields per entry

Every entry uses this exact template. **An entry missing any required field is malformed and must not be added.**

```
### <key>  [<status>]
- **Builds on:** <one or more specific section pointers into engine / receipts / prior-art / frontier / units>
- **Description:** <one paragraph describing the application — what it is, what it does, how it uses the core>
- **Gates:** <concrete criterion that would move this entry to the next status>
- **Gated on:** <current blocker, if any — optional>
- **External deps:** <relevant tools, formats, libraries — optional>
```

Field rules:

- `<key>`: kebab-case, unique within this doc (including archived entries). No whitespace, no slashes, no quotes.
- `[<status>]`: exactly one of `[noted]` / `[sketched]` / `[developed]` / `[archived]`. See STATUS LADDER.
- **Builds on**: at least one pointer to a **specific named section** in a core doc. Format: `engine <SECTION>`, `receipts §<entry-name>`, `prior-art \`<pa-key>\``, `frontier \`<key>\``, `units §<n>`. Generic pointers like "the framework", "Character", or "the deformation" are **invalid** — the entry must name what it uses.
- **Description**: descriptive language only (uses verbs like *render / demonstrate / apply / illustrate / compute / display / build / visualize / simulate / pedagogically present*). Avoids structural verbs (see ANTI-DRIFT Check 1). One paragraph; longer goes in `sketched` or earns a dedicated doc.
- **Gates**: must be a concrete criterion, not a vibe. Example: "Move to `sketched` when a named substrate has been worked through." Not: "Move to `sketched` when more is clear."
- **Gated on**: optional. Names the current blocker (e.g., "the verticals' reads working", "presentation pipeline online").
- **External deps**: optional. Useful for entries that depend on specific tools (Blender, Three.js, particular file formats, etc.).

---

## STATUS LADDER — values and transitions

| status | meaning | content size in this doc |
|---|---|---|
| `[noted]` | recorded; the idea exists; no concrete elaboration | one paragraph (≤ ~200 words) |
| `[sketched]` | has concrete specifics — algorithm, named substrate, pseudocode, numerical estimate, format choice, or worked example | 200–800 words |
| `[developed]` | thick enough to deserve its own treatment doc `mpa_<key>.md`; this entry becomes a stub pointing at it | stub in this doc; full content in linked doc |
| `[archived]` | superseded, dropped, or determined irrelevant; kept as a tombstone so it isn't re-derived | 1–2 sentences with reason |

**Transitions (each requires a recorded trigger):**

- `noted → sketched`: at least one concrete specific is added — an algorithm sketch, a named substrate worked through, pseudocode, a numerical estimate, or a chosen data format. Update the `Gates` field to reflect what would move it to `developed`.
- `sketched → developed`: content has grown beyond ~500 words of substantive elaboration **AND** a dedicated treatment doc `mpa_<key>.md` is created (pattern set by `character_fdr_treatment.md`). The entry in this doc becomes a stub: schema fields + a one-line "see `mpa_<key>.md`".
- `→ archived` (from any status): item is superseded by another entry, dropped after consideration, or determined irrelevant. Set status to `[archived]` and add a one-sentence reason in the `Description` field. **Do not delete archived entries** — tombstones prevent re-derivation.

---

## ANTI-DRIFT — the five checks (run on every proposed entry)

Before adding any entry, run these five checks. **If any check fires, the entry has a structural component that does not belong here.** The correct response is to *split*: route the structural piece to `character_frontier.md` (typically the steeping rung) and keep only the application-side content in this doc.

### Check 1 — verb test (structural language)

Does the entry's `Description` or `Gates` use verbs in load-bearing position from this list:

> *implies, proves, shows that, demonstrates that, requires, forces, predicts, entails, falsifies, kills, fails if, must, cannot, claims, asserts, establishes, derives*

If yes → the entry is asserting structure, not applying it. **Route the structural assertion to frontier.**

(Note: structural verbs may appear when *quoting* core content — e.g., "uses the iff-chain that forces a triad" is fine because the entry is referencing an existing core claim, not making one. The test is whether the entry is the *source* of the assertion.)

### Check 2 — kill-condition test

Does the entry contain a falsifier, kill condition, observable threshold below which something fails, or any "this would refute X" language?

If yes → falsifiers belong in `engine FALSIFIERS` or in `receipts §<entry>` (operationalized by `frontier battery:<key>`), never here. **Route to frontier.**

### Check 3 — coined-object test

Does the entry redefine, extend, modify, or rename any of these coined framework objects?

> **the ch unit · chit · trail (and trail vector) · holding · coherence · the c/s/r regime semantics · k_frust · the two faces · the two bits · the bit-chit correspondence · the Central Commitment · the Two-Frame Construction · the deformation · mpa-legal · the chimeric sign · the Banach reference**

If yes → coined objects are owned by `character_engine.md` and the prior-art residual. **Route any redefinition to frontier.**

### Check 4 — anchor specificity test

Does the `Builds on` field name **specific sections**, or does it use generic language ("the framework", "Character", "the core", "the deformation calculus")?

If generic → the anchor doesn't constrain the entry. **Require specific section names before adding.** If the user can't name specific sections, the item probably isn't ready to be an application yet (it may be a framework-level idea that belongs in frontier steeping).

### Check 5 — substitution test

Could a sentence from the entry's `Description`, quoted verbatim into a core doc, change the meaning of that core doc?

If yes → the entry is doing structural work. **Split**: route the structural sentence(s) to frontier, keep only the application content here.

---

## ROUTING TABLE — worked examples for ambiguous cases

For an AI applying these rules to new items, here is the routing for common patterns:

| pattern | example | routing |
|---|---|---|
| Rendering / visualization of an existing structural claim | "VDM map of character" | **applications**, `noted` |
| Pedagogical illustration of an existing framework concept | "interactive animation of c→s→r migration" | **applications**, `noted` |
| Specific substrate computation (using existing machinery) | "glass_two_step worked through with current pipeline" | **applications**, `sketched` (it has a named substrate) |
| Simulation protocol applying existing falsifiers | "running battery:sign-interior on Veenstra metamaterial" | **applications**, `sketched` |
| Presentation / slide structure | "10-slide intro to two-frame for cond-mat audience" | **applications**, `noted` |
| Computational notebook walking through ch derivation | "Jupyter notebook deriving 1 ch = ln 2 from Q-peak" | **applications**, `sketched` |
| Proposed new framework structure | "I think there's a third face" | **frontier steeping** (pure-exploration); not applications |
| Proposed new falsifier | "Here's a test that would kill the two-frame iff" | **frontier battery** or **engine FALSIFIERS**; not applications |
| Proposed redefinition of a coined object | "Maybe ch should be ln 3 not ln 2" | Reject — ch is forced (`character_units.md §1`). Not anywhere unless a derivation error is found, in which case frontier `corrected`. |
| Reveals a gap in the core | "Applying VDM to k_frust would need a new observable we don't have" | **frontier steeping** (the gap); then **applications** entry can build on the gap once it's filled |
| Tool / library workflow | "Blender add-on for rendering Character substrates" | **applications** with `External deps`, `noted` |
| Vague idea, no anchor possible | "What if Character applied to consciousness" | Reject from applications (no specific anchor). If it has a concrete mechanism + falsifier, route to **frontier steeping**. Otherwise the discipline rejects it. |

When a proposed item doesn't match any row above, default behavior:

1. Run all five ANTI-DRIFT checks.
2. If all pass and `Builds on` resolves to a specific section → applications, default status `noted`.
3. If any check fires → split per the check's routing.
4. If `Builds on` cannot be specified → reject the entry; ask the user one clarifying question about which core elements it builds on.

---

## AUTHORING PROCEDURE — step-by-step (for any AI to follow on new items)

When a user proposes adding an item to this doc:

1. **Read the proposed item carefully.** Identify what it actually is — a rendering? a pedagogical use? a computation? a workflow? something else?

2. **Determine core anchors.** Name specific sections of engine / receipts / prior-art / frontier / units that the item uses. Write them down explicitly. If you cannot name specific sections, ask the user one clarifying question before proceeding.

3. **Run all five ANTI-DRIFT checks** in order. For each check:
   - If it fires, stop and report which check fired.
   - Identify the structural piece(s) and the application piece(s).
   - Propose a split: structural pieces go to `character_frontier.md`; application pieces stay here.
   - Wait for user confirmation before making any edits.
   - If split-routing succeeds, the structural piece becomes a frontier entry first; the application entry here can then `Builds on` the new frontier item.

4. **Determine status** per STATUS LADDER:
   - Short, no specifics → `noted`.
   - Has concrete specifics → `sketched`.
   - Has dedicated doc → `developed`.
   - Superseded/dropped → `archived`.

5. **Write the entry** in the SCHEMA template. Fill all required fields.

6. **Run INVARIANTS check** (below) on the new entry. All must pass.

7. **Insert** in the REGISTER section in **alphabetical order by key**. Archived entries go in ARCHIVED, also alphabetical.

8. **Report** to the user:
   - The key and status.
   - The core anchors used.
   - Any ANTI-DRIFT checks that fired and how they were routed.
   - Confirmation that all six INVARIANTS pass.

---

## INVARIANTS — auditable (verify after every edit)

- **A1 — anchor required.** Every entry has at least one `Builds on` pointer that resolves to an existing section in a core doc. No orphans.
- **A2 — schema complete.** Every entry has all required fields: key, status, Builds on, Description, Gates.
- **A3 — no structural claims.** No entry's `Description` or `Gates` uses structural verbs (ANTI-DRIFT Check 1) in load-bearing position; no entry contains kill conditions (Check 2) or redefinitions of coined objects (Check 3).
- **A4 — status valid.** Status is exactly one of the four allowed values.
- **A5 — developed → external doc.** Every `developed` entry has a linked dedicated treatment doc `mpa_<key>.md` and is a stub in this doc.
- **A6 — unique keys.** No two entries share a key (including across REGISTER and ARCHIVED).

The AI making the edit verifies these invariants mechanically before reporting completion. If any fails, the edit is malformed and must be corrected.

---

## REGISTER

### vector-displacement-map  [noted]

- **Builds on:** engine TWO FACES (2-vector field over substrate, components = the two independent faces); engine TWO-FRAME CONSTRUCTION (measurement values for the components — $X$ for the amplitude face, $\mathcal{T}$ for the sign-topological face); engine TWO BITS (independence of the faces guarantees the 2-vector is irreducible, not collapsible to a scalar).
- **Description:** Character at each point of a substrate can be rendered as a 2-vector deviation from the Banach reference, with components (amplitude-face deviation, topological-face deviation). The natural visualization is a vector displacement map (VDM) — carrying direction (which face moved) and magnitude (how much). A normal map or scalar height map collapses both deviations into one fake-lighting perturbation and loses which face moved. The Banach ray is the undisplaced reference surface; substrates displace it.
- **Gates:** Move to `sketched` when either (a) a concrete VDM format/encoding is specified for at least one named substrate, or (b) a rendered example exists driven by earned-vertical reads.
- **Gated on:** the verticals' reads working (`laser_ro_nominal_v1`, `banach_frustrated` / `three_species_cycle`, `glass_two_step`). Current live blocker in test session.
- **External deps:** TBD (likely OpenEXR or similar HDR vector-channel format; Blender / Houdini / Three.js for rendering).

---

## ARCHIVED

*(none yet)*
