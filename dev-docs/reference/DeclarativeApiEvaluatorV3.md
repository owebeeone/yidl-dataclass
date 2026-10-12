# Declarative API Evaluator & Identifier — v3

File `DeclarativeApiEvaluatorV2.md` is the second *file* revision of this instrument. It supersedes
[DeclarativeApiEvaluator.md](DeclarativeApiEvaluator.md), which labels itself v2 internally, so the
instrument here is internally **v3**. The changes implement
[DeclarativeApiEvaluator-reviewF51.md](DeclarativeApiEvaluator-reviewF51.md). Motivation:
[DeclarativeManifesto.md](DeclarativeManifesto.md). Descriptive corpus:
[DeclarativePatternSurvey.md](DeclarativePatternSurvey.md) (optional background; this document is
self-contained and cites no external finding numbers).

**What it is.** A normative instrument applied to a candidate declarative API / DSL ("DAPI") to
**(A) identify** it, **(B) place** it as the triple **(Δ.1, Δ.2, C)** — gap richness, generativity,
correctness envelope — **(C) check** it against measurable floors, and **(F) rank** candidates as a
Pareto frontier. It doubles as the fitness function for an LLM design loop. **Every score names its
evidence; a field without evidence is reported `unscored`, never 0.**

## What changed from v2

1. **C is constructible.** Outcomes are assigned per class of a shared, versioned **reference error
   taxonomy** (Appendix A) under a declared **author model** (`llm` | `human`), so every candidate
   partitions the same mass and `deleted` is bounded. Bins are **detection stages relative to a
   declared ship boundary**. C is a continuous total function for the loop and banded only for the
   report. Spurious rejection (completeness cost) is scored. A `static` claim not backed by a
   passing mutant is downgraded to where the mutant was actually caught.
2. **Δ is property-based and never averaged.** Δ.1 is a vector (locality, search, staging) plus a
   measured expansion ratio; Δ.2 is a ladder of *what is derived rather than declared*. No level is
   defined by a named system. The position is the triple, not a mean.
3. **Frontier, not corner.** The scalar loss and the four quadrants are gone. Output is the Pareto
   frontier over (Δ.1, Δ.2, C) under declared floors. Regularizers are measurable floors: semantic
   definition, explainability, predictable compositionality, escape containment, oracle
   independence, held-out coverage.
4. **New dimensions.** Engine failure semantics, evolution posture, engine cost (logged); an
   LLM-loop panel (schema-capturable share, spec-in-context cost, few-shot curve, repair cost,
   message actionability, edit-proportionality, partial-program validation).
5. **Gate repaired.** Order-dependence is graded (only *ambient* fails); "say only the delta" moved
   out of the gate into R7; there is no gate total.
6. **Seams are scored** as their own row; a bundle's surfaces are never averaged and the boundary
   between them is never dropped.
7. **Design-stage mode** scores *gate specifiability* and reports C as an interval, never a point.
   A **desk** mode exists for inspection-only scoring and is labelled as such.
8. **Calibration protocol**: pre-registered anchors, a held-out set, blind second-rater agreement,
   and a rule for when the rubric may change.

## Premises (self-contained)

- **P1 Two properties, not one.** Declarativeness (what the engine derives for you) and correctness
  (what is caught before it ships) are independent properties of a surface. Report both; never
  collapse them into one grade.
- **P2 Denotation.** A description has a meaning definable independently of the engine that
  executes it. Where that meaning is only "whatever the engine does", correctness is undefined.
- **P3 Generativity costs predictability.** The more wiring the engine derives per instance, the
  harder it is to gate statically and to predict. The instrument must see both sides.
- **P4 Archetype is a prior.** A reconciler, solver, cascade, resolver, or compiler predicts the
  *shape* of its failures. The archetype selects which failure classes are live; it never sets an
  outcome.
- **P5 Denotations are not oracles.** Two ways of computing the same meaning are an oracle only
  when a harness cross-checks them.
- **P6 Measurement means agreement.** Two raters applying the instrument to the same artefact must
  get the same numbers. Every field carries the evidence that produced it.

## How to use it

0. **Declare inputs** (A.0): taxonomy version, author model, intent corpus with held-out split,
   implementation and version, ship boundary, archetypes, floors. Freeze them before scoring.
1. **Identify & scope** (Part A): choose the unit, name seams, run the gate.
2. **Position** (Part B): Δ.1, Δ.2, then C from the per-class outcomes.
3. **Regularizers** (Part C): R1–R7 and closure.
4. **Log** (Part D): engine properties, evolution, cost.
5. **LLM-loop panel** (Part E) when an authoring harness exists.
6. **Output** (Part F): frontier membership under floors; scalar only if weights are declared.
7. **Calibrate** (Part G) whenever the instrument or an anchor changes.
8. Fill the **template** (Part H).

## Part A — Declarations, unit, seams, gate

### A.0 Step-0 declarations (fixed before any score is written)

| Declaration | Requirement |
|---|---|
| `RET` | Reference error taxonomy version (Appendix A), plus any domain extension by name and version. |
| `author` | `llm` or `human`. Determines taxonomy weights. Report `llm` as primary for design-loop use; add a `human` histogram when the DSL is also human-authored. |
| `implementation@version` | The toolchain scored. C is a property of language *plus* toolchain; two engines for one language get two cards. |
| `mode` | `measured` (mutants executed), `desk` (outcomes assigned by inspection, no execution), `design-stage` (no engine exists; B.3.4). |
| `ship boundary` | The point after which effects are observable by users or persisted. Decides whether `load` is pre-ship. |
| `archetype(s)` | Which engine archetypes the surface contains (cascade, resolution, solver, planner, reconciler, lowering, dataflow, templating). Selects the live E-classes. |
| `intent corpus` | ≥ 30 intents from an exogenous source (users, tickets, substrate docs, prior hand-coded solutions), frozen before design iteration, ≥ ⅓ held out and never used to tune defaults. Each intent carries: id; natural-language statement; canonical minimal structured intent (for R7); oracle expectation; tags naming the RET classes it can exercise. |
| `floors` | Defaults from Part F or declared overrides, with the domain reason. |

### A.1 Unit of evaluation — a coherent gap-owning surface

Score a **surface**, never a framework. A surface is coherent iff it has **(i) one denotation
function, (ii) one gate, (iii) one escape boundary**. Where any of the three differs, split, and
name each piece. A piece that fails the gate (A.3) is reported as `split-off: imperative
(gate-failing)` and is not scored on Part B. Never average pieces.

### A.2 Seams

The boundary between two pieces of a bundle (declarative ⊕ imperative, or two declarative
surfaces) is a **seam** and gets its own row (B.3.5). The characteristic bugs of bundled systems
live at the seam, not in either half.

### A.3 Gate — is it a DAPI?

Three checks. No total. Pass = both definitional checks pass **and** the non-triviality check
passes.

- **Order-dependence (definitional, graded).** Does a fragment's meaning depend on evaluation or
  declaration order?
  - `absent` — pass.
  - `explicit-and-local` — order matters only where the description says so, and only within a
    bounded scope (an explicit precedence list, a declared dependency). Pass.
  - `ambient` — meaning depends on order the author did not declare and cannot see. **Fail.**
- **Programs-as-data (definitional).** The surface is a description that can be inspected,
  transformed, and compared before it runs; not a sequence of effects. Pass/fail.
- **Δ > 0 (non-triviality).** The engine performs at least one of: *resolution* (Δ.1 ≥ 1),
  *derivation* (Δ.2 ≥ 1), or *structural expansion* (one description element lowers to more than
  one substrate operation). Pass/fail, with the evidence named. Fail ⇒ veneer or
  imperative-in-disguise.

`imperative-in-disguise` is a **gate result**, never a position. A gate-passing surface with low
Δ.1 and Δ.2 is a thin DAPI, which is a position, not a verdict.

## Part B — Position (Δ.1, Δ.2, C)

### B.1 Δ.1 — gap richness (0–6, reported as a vector)

Score three properties a stranger can check. **Δ.1 = L + S + T.** Report the vector and ρ.

**L — locality.** The widest span of the description the engine must read to resolve one element.
- 0 *local*: an element's lowered form depends only on itself (marshaling, templating).
- 1 *scoped*: depends on its enclosing scope or on elements it names (name binding, inheritance,
  context lookup).
- 2 *global*: depends on the whole description or on external state (a cascade over all rules,
  whole-graph solving, reconciliation against live state).

**S — search.** Whether resolution is a lookup, a derivation, or a choice.
- 0 *mapping*: fixed one-to-one or table-driven translation.
- 1 *derivation*: deterministic multi-step computation with a unique result (dependency ordering,
  type inference, precedence resolution, plan derivation with no alternatives).
- 2 *search*: the engine chooses among alternatives under constraints or an objective (constraint
  solving, cost-based optimisation, layout solving, matching).

**T — staging.** The number and shape of resolution phases.
- 0 *single pass*.
- 1 *multi-pass, feed-forward*: each pass completes before the next (parse → resolve → lower).
- 2 *iterative*: fixpoint, feedback, or reconciliation loops; incremental re-evaluation on change.

**ρ — expansion ratio.** Size of the lowered substrate output ÷ size of the description, in one
declared unit (tokens, AST nodes, or substrate operations), median and range over the intent
corpus. ρ is the objective proxy for "vocabulary added minus substrate vocabulary". It is reported
alongside Δ.1, not added to it.

### B.2 Δ.2 — generativity (0–5): what is derived rather than declared

Score the **highest class the engine performs routinely** on the intent corpus (present in at
least one in ten corpus programs); report the set of classes present. Levels are mechanism
classes; the parenthetical examples are illustrations, not anchors.

- 0 *explicit*: the author wires everything.
- 1 *defaults*: omitted elements receive engine-supplied values.
- 2 *reference resolution*: named references or injections are bound by the engine, by name, type,
  or id.
- 3 *contextual selection*: the binding chosen depends on where the element sits (scope, ancestor,
  environment, qualifier, platform).
- 4 *transitive derivation*: the engine derives chains the author never named (dependency closure,
  propagated parameters, inferred ordering).
- 5 *topology derivation*: the wiring graph itself is constructed per instance from declared
  capabilities, constraints, or matchers; the author declares parts and rules, the engine builds
  the assembly.

Δ.1 and Δ.2 are **never averaged**. A (5, 2) and a (2, 5) are different systems and stay
different on the card. If plotting, normalise each axis to [0, 1].

### B.3 C — correctness envelope

#### B.3.1 Inputs

The RET (Appendix A) restricted to the declared archetypes gives the **live class set** with
weights `w_k` summing to 100 for the declared author. The intent corpus supplies the programs to
mutate.

#### B.3.2 Outcome per class

For each live class `k`, assign exactly one outcome and its evidence:

| Outcome | Meaning | Required evidence |
|---|---|---|
| `absent` | The *legitimate intent* this class perturbs cannot be expressed in the surface at all. Excluded from C; its mass goes to coverage (R6). | The held-out intents it blocks. |
| `deleted` | The intent is expressible and the footgun is **unexpressible by construction**. | The footgun class, an attempt to write the mutant, and why it cannot be written. |
| `decode` | Rejected by grammar or schema alone. | The schema rule. |
| `validate` | Rejected by the static gate before the ship boundary. | The check that catches it, by name from the gate inventory. |
| `load` | Rejected at deploy, plan, or dry-run **before effects**. Counts as pre-ship only if the workflow guarantees the step; otherwise classify as `first-run`. | The step and its enforcement. |
| `first-run` | An error signal at first exercise of the affected path. | The observed signal. |
| `latent` | An error signal only under conditions not met at first exercise (rare branch, scale, time). | The triggering condition. |
| `silent` | A wrong result with no error signal at any time. | What the program does instead; whether R2-level provenance would reveal it. |

The `deleted`/`absent` line: **can the legitimate intent be expressed?** Yes ⇒ the class is live.
No ⇒ `absent`.

**Downgrade rule.** In `measured` mode each non-`absent`, non-`deleted` outcome is backed by at
least one executed mutant. A `validate` or `decode` claim whose mutant passes the gate is
reclassified to the stage where it was actually detected. Gate unsoundness therefore lands in the
histogram automatically; it is never a footnote.

#### B.3.3 Aggregates and C

Renormalise the non-`absent` masses to 100. Then:

```
left_w    = deleted + decode + validate + load          (pre-ship)
silent_w  = latent + silent                             (post-ship, no timely signal)
κ         = fraction of held-out VALID programs the gate rejects   (completeness cost)

C_cont    = clamp(0, 5,  5 · (left_w + 0.5 · first-run) / 100  −  5 · κ)

cap       = 2 if silent_w ≥ 40 ; 3 if silent_w ≥ 25 ; 5 otherwise
C_band    = min( round-half-up(C_cont), cap )
```

`C_cont` is total, continuous, and monotone: full credit for pre-ship detection, half for
first-run, none for anything without a timely signal, minus spurious rejection. The cap preserves
"silent mass dominates" in the report. **The design loop consumes `C_cont`, `left_w`, `silent_w`,
and `κ`; it never sees the band.** Also report `diagnosable_w`: the share of `silent_w` for which
the wrong result is attributable given the surface's R2 level (informational; explainability is
scored as R2, not folded into C).

**Temporality remains a prior.** No outcome is assigned from the archetype. The archetype only
selected which E-classes are live.

#### B.3.4 Design-stage mode (no engine exists)

Score **gate specifiability**, not intent. For each live class: `specified(stage)` if a *written
decision procedure* exists that would catch it at that stage, shipped with the mutant that would
test it; `unknown` if only an intention exists; `deleted(projected)` with the unexpressibility
argument; or `absent`. Compute `C_opt` with `unknown` counted as `validate` and `C_pess` with
`unknown` counted as `silent`, κ = 0 flagged. Report **`C ∈ [C_pess, C_opt] (projected)`**. A
projected interval never sits on a measured axis without the flag and never counts toward "a
measured candidate reaches the floors".

`desk` mode (inspection without executing mutants) reports `C_band` only, flagged `(desk)`, and
is not frontier-eligible.

#### B.3.5 Seam row

For each seam named in A.2, apply the RET classes flagged `seam` (U11, U12, U16, and E-D2 where
dataflow is present) to programs that cross the boundary. Report `seam_silent_w` on its own line.
A seam is never averaged into either surface.

## Part C — Regularizers (measurable floors)

Each regularizer is scored 0–5 from a stated measurement and compared with its floor (Part F).
Failing a floor removes a candidate from the frontier; it does not change its position.

**R1 Semantic definition** — is meaning defined independently of the engine?
0 meaning is whatever the engine does · 1 prose · 2 examples or golden outputs · 3 executable
reference semantics or an independent second engine · 4 formal / denotational definition · 5
formal plus mechanised conformance.

**R2 Explainability / provenance** — can the engine say *why*?
0 none · 1 logs · 2 dry-run or plan diff · 3 per-result provenance ("why this value") · 4
counterfactual ("what changes if") · 5 queryable model of the resolved state.

**R3 Predictable compositionality** — negative surprise on combination.
Count `F` = features (the card states the counting unit: constructs, keywords, attributes) and `I`
= interaction clauses: documented rules conditioned on the co-presence of two or more features
("when X is combined with Y"), plus every U12 mutant that came out `silent` (an undocumented
interaction). `q = I / F`. 5: q ≤ 0.1 · 4: ≤ 0.25 · 3: ≤ 0.5 · 2: ≤ 1 · 1: ≤ 2 · 0: > 2.

**R4 Escape containment** — not escape rate.
Classify escapes: *hermetic* (declared interface; cannot affect declarative semantics outside its
own node) · *leaky* (can mutate state the engine reads) · *global* (can change engine behaviour);
and *visible* (distinct, grep-able syntax) or *invisible* (looks like ordinary vocabulary).
5: hermetic, visible, and needed for ≤ 5 % of held-out intents · 4: hermetic and visible · 3:
hermetic-invisible or leaky-visible · 2: leaky-invisible · 1: global-visible · 0: global-invisible.
Log `e` = share of held-out intents needing any escape.

**R5 Oracle independence** — the anti-private-language anchor.
0 none · 1 self-consistency · 2 tests or examples written from the designer's own understanding
(golden *intent* counts here, not at 3) · 3 golden outputs from an independent source (domain
expert, exogenous spec, prior hand-coded solutions) · 4 differential harness against an
independently built engine or the substrate · 5 N independent projections cross-checked against an
exogenous substrate, realised as a running harness. Multiple denotations without a harness score
as if there were one (P5).

**R6 Held-out coverage.**
`cov` = share of held-out intents expressible within the declarative surface (escapes do not
count). 5: ≥ 95 % · 4: ≥ 85 % · 3: ≥ 70 % · 2: ≥ 50 % · 1: ≥ 25 % · 0: below. Log the worst-case
expression ratio. `absent_w` from B.3.2 lands here.

**R7 Representational efficiency** (formerly the gate's "say only the delta").
`r` = description size ÷ canonical minimal intent size, median over held-out intents, one declared
unit. 5: r ≤ 1.2 · 4: ≤ 1.5 · 3: ≤ 2 · 2: ≤ 3 · 1: ≤ 5 · 0: > 5. Also report
**delta-proportionality**: rank correlation between description size and deviation-from-default
size across the corpus (≥ 0.7 expected of a "say the delta" design), and the worst-case `r`.
Because compact-by-default designs push mass into RET class U8 (wrong default assumed), R7 and C
now trade off visibly.

**Closure (0–2, tie-breaker only).** Is a compound built from parts itself a first-class part
usable to build larger ones? 0 no · 1 partially (some compounds are closed) · 2 yes, with
user-defined abstraction. Never a floor, never disqualifying.

## Part D — Logged dimensions (unscored, always reported)

- **D1 Engine properties**, each `yes | no | partial` with evidence: *total* (every valid program
  has a defined result), *deterministic* (same input, same output across runs and machines),
  *idempotent* (re-applying changes nothing; reconcilers), *reproducible* (results pinned to
  versions). The canonical failures of each archetype are already in the histogram as E-classes;
  D1 records the engine's stated contract.
- **D2 Evolution posture**: is a semantic version pinned in the description; are default changes
  diffable; is there a plan or dry-run across versions; deprecation posture (`none` | `warn` |
  `period` | `never-break`). Second-order for a design loop, first-order for anything shipped.
- **D3 Engine cost**: spec size (tokens or pages), engine size (LOC), and the share of engine
  behaviour exercised by the R5 harness. Without this a loop is free to propose engines nobody can
  build correctly.
- **D4 Extrinsic familiarity**: training-corpus familiarity of today's models. Logged, never
  scored; it is a property of the models, not the language.

## Part E — LLM-loop measurables

Properties of the language, measurable with an authoring harness. Without a harness, report
`unscored`.

- **E1 Schema-capturable share** = `decode` mass ÷ 100. The cheapest gate that exists; the
  fraction of the envelope reachable by constrained decoding.
- **E2 Spec-in-context cost**: tokens of the minimal specification plus examples an authoring model
  needs to reach the E3 target. A language with a perfect gate can still be un-authorable.
- **E3 Few-shot curve**: oracle-pass rate on held-out intents at k ∈ {0, 1, 3, 10} examples; report
  `k80`, the smallest k reaching 80 %.
- **E4 Repair cost**: median iterations and median edit tokens from a detected-error mutant to an
  oracle-passing program, using the toolchain's actual messages. This is the number the loop cares
  about; it combines C, locality, and message quality.
- **E5 Message actionability** (0–3): 0 none · 1 names the location · 2 location and error class ·
  3 location, class, and a fix.
- **E6 Edit-proportionality**: median (description diff tokens ÷ intent-change tokens) over an
  edit corpus of intent pairs. Delta-proportionality for edits, which is how an agent works.
- **E7 Partial-program validation**: can an incomplete description be checked, so the author gets
  signal mid-construction? `yes | no`.

## Part F — Output: frontier under floors

**Objectives (maximise):** Δ.1 (0–6), Δ.2 (0–5), C_cont (0–5).

**Default floors** (override per domain on the card, with the reason):

| Floor | Default | Why |
|---|---|---|
| R5 oracle independence | ≥ 3 always | Anti private-language collapse; the exogenous anchor. |
| R2 explainability | ≥ max(0, Δ.2 − 2) | The explanation floor rises with generativity (P3). |
| R3 predictable compositionality | ≥ 3 | Generativity must not be bought with surprise. |
| R4 escape containment | ≥ 3 | No global escapes. |
| R6 held-out coverage | ≥ 3 | A DSL that expresses only its design corpus is overfit. |
| Reporting rule | `C_band = 5` requires R1 ≥ 3 | "Cannot ship broken" is undefined when meaning is defined by the engine; otherwise report 4 and note the cap. |

**Dominance.** Among floor-passing candidates in `measured` mode, A dominates B iff A ≥ B on all
three objectives and > B on at least one. Report the non-dominated set as the frontier. Candidates
failing a floor are listed below the line with the failed floor named. `design-stage` cards are
listed with their interval and `(projected)`; `desk` cards with `(desk)`; neither is
frontier-eligible.

**The target.** "Top-right" is replaced by *the frontier region that satisfies the floors*.
Whether any measured candidate occupies it is a result of the corpus run, never an axiom.

**Scalar (optional).** Only with user-declared weights, printed on the card:
`scalar = a·Δ.1/6 + b·Δ.2/5 + c·C_cont/5, (a, b, c) = …`. There is no default scalar.

**Tie-breakers** among frontier points, in order: higher closure; lower E2; lower E4.

**Loop signal.** A design loop consumes `C_cont`, `left_w`, `silent_w`, `κ`, and the raw
regularizer measures (`q`, `e`, `cov`, `r`), never bands. This removes the gradient asymmetry that
made a banded C invisible to the loop while Δ moved continuously.

**Goodhart guards**, each measurable: `deleted` must cite a footgun class with an attempted mutant
(B.3.2); Δ.2 inflation is charged by the R2 and R3 floors; relabelling `absent` is charged by R6;
tuning defaults to the design corpus is charged by scoring R6 and R7 on the held-out split only.

## Part G — Calibration protocol

1. **Pre-register anchors.** Before scoring, choose ≥ 6 anchor surfaces, preferably public, covering
   ≥ 3 archetypes and the full Δ.2 range. Publish their cards with the instrument version.
2. **Hold out.** Keep ≥ 3 surfaces that are never used to tune anything. Score them last, after the
   rubric is frozen, and publish without adjustment.
3. **Second rater.** Every card is re-scored blind by a second rater (a person or a different
   model) from the same Step-0 declarations. Report per-field exact agreement and rank correlation
   for Δ.1, Δ.2, and C_cont across the set. A card whose C_cont disagreement exceeds 1.0 is
   re-mutated, not averaged.
4. **Rubric change rule.** A change is admissible only when a disagreement is traceable to
   ambiguous rubric text. "The ranking looks wrong" is a finding about the anchors or the premises,
   not a licence to edit the rubric. Every change bumps the instrument version and invalidates all
   cards.
5. **Re-score** anchors after every change; the held-out set last.

## Part H — Scorecard template

```
DAPI surface: <name>          implementation@version: <>        substrate: <lowers into>
mode: measured | desk | design-stage     author: llm | human     ship boundary: <declared>
RET: v1 [+ <domain>-ext vN]   intent corpus: <id/version> (n=__, held-out=__)   archetype(s): <>
floors: <defaults | overrides + reason>   rater: <>   second rater: <>   agreement: <>

A. UNIT & GATE
   unit: <surface>    split-off: <pieces, gate result>    seams: <named>
   order-dependence [absent | explicit-local | ambient]   programs-as-data [y/n]   Δ>0 [y/n: evidence]
   -> is-a-DAPI [y/n]
   gate inventory: <checks the toolchain performs: schema, references, types, cycles, satisfiability, …>

B. POSITION
   Δ.1 = __ /6   (L __, S __, T __)    ρ = __ median, __–__ range (unit: <>)
   Δ.2 = __ /5   classes present: {…}
   C_cont = __    C_band = __  [cap: silent | R1 | none]    κ = __
   masses (absent excluded, sum 100): deleted __ decode __ validate __ load __ first-run __ latent __ silent __
   left_w __   silent_w __   diagnosable_w __   absent_w __ (→ R6)
   design-stage only: C ∈ [__, __] (projected)   unknown classes: <list>
   seam rows: <seam>: seam_silent_w __ (classes …)

C. REGULARIZERS                                      floor   pass?
   R1 semantic-definition            __ /5            —
   R2 explainability                 __ /5            __      __
   R3 predictable-compositionality   __ /5  (q = I/F = __/__)   __   __
   R4 escape-containment             __ /5  (class <>, visible y/n, e = __)   __   __
   R5 oracle-independence            __ /5            __      __
   R6 held-out coverage              __ /5  (cov __ %, worst r __)   __   __
   R7 representational               __ /5  (median r __, delta-prop __, worst r __)
   closure                           __ /2

D. LOGGED
   engine: total __  deterministic __  idempotent __  reproducible __
   evolution: version-pinned __  default-diff __  cross-version-plan __  deprecation <>
   engine cost: spec __ tokens   engine __ LOC   harness coverage of engine __ %
   extrinsic familiarity: <>

E. LLM-LOOP
   schema-capturable __ %   spec-in-context __ tokens   k80 = __
   repair cost __ iters / __ tokens   message actionability __ /3
   edit-proportionality __   partial-program validation [y/n]

F. OUTPUT
   floors: <all pass | failed: …>    frontier member [y/n]    dominated by: <>
   scalar (only if weights declared): __ with (a, b, c) = <>
   silent bug-debt: <the silent and latent classes, enumerated>
   biggest lever: <the single change that moves the position most>

Evidence: <paths: mutants, corpus, harness, spec sections>
```

## Appendix A — Reference error taxonomy, RET v1

**Rules.** Weights are tiers: H = 3, M = 2, L = 1 points, per author. Include the U-classes always
and the E-classes only for the declared archetypes; domain extensions add `X-n` classes with a
declared tier and their own version. Normalise the included points to 100. Extend by adding classes
with a version bump; never remove or re-tier a class within a version.

### Universal authoring classes (U)

| id | class | example mutant | seam | llm | human |
|---|---|---|---|---|---|
| U1 | Unknown vocabulary (misspelled or non-existent keyword or field) | `colour:` for `color:` | | M | H |
| U2 | Wrong type or shape (scalar for list, object for string, wrong nesting) | `ports: 80` for `ports: [80]` | | H | M |
| U3 | Missing required element | omit the target of a binding | | M | M |
| U4 | Dangling reference (named thing not declared) | `db-main` when only `db_main` exists | | H | M |
| U5 | Ambiguous reference (several candidates; the engine picks) | two providers satisfy one injection | | M | L |
| U6 | Valid-but-wrong value (right type, wrong meaning) | wrong enum member, wrong sign | | H | H |
| U7 | Unit or magnitude error | `timeout: 30` seconds where milliseconds are expected | | M | H |
| U8 | Wrong default assumed (element omitted believing the default is X; it is Y) | omit `restart:` expecting `always` | | H | M |
| U9 | Duplicate or conflicting declarations | one key declared twice with different values | | M | M |
| U10 | Ordering assumption (order matters when it does not, or vice versa) | relying on file order for precedence | | M | M |
| U11 | Wrong scope or context (leaks, shadows, or is invisible) | a per-request binding declared globally | seam | M | M |
| U12 | Feature interaction (two valid features combined produce an unintended result) | `inherit` and `override` on one element | seam | H | M |
| U13 | Hallucinated construct (a plausible whole construct that does not exist) | `retry: exponential` where no retry exists | | H | L |
| U14 | Convention drift (an idiom from another DSL or older version; valid here, means something else) | another tool's `depends_on` semantics | | H | L |
| U15 | Version mismatch (construct valid only in another version) | a field removed in the pinned version | | M | M |
| U16 | Escape misuse (an imperative escape breaks a declarative invariant) | a hook mutates state the engine owns | seam | M | M |
| U17 | Incomplete program silently completed (the engine fills what the author forgot) | omitted constraint → unconstrained solve | | H | M |
| U18 | Identity collision (two declarations resolve to one identity) | two resources normalise to one name | | M | M |

### Archetype classes (E) — tier M for both authors unless a domain extension says otherwise

| archetype | id | class |
|---|---|---|
| cascade | E-C1 | Precedence conflict resolved unexpectedly (two rules match; the wrong one wins) |
| cascade | E-C2 | Specificity escalation (the author adds specificity to force a win) |
| cascade | E-C3 | Inheritance leak (a value inherited where not intended) |
| resolution | E-R1 | Resolution cycle |
| resolution | E-R2 | Missing binding discovered at resolution time |
| resolution | E-R3 | Lifetime or scope mismatch (singleton where per-instance was meant, or the reverse) |
| solver | E-S1 | Unsatisfiable set (no solution) |
| solver | E-S2 | Under-constrained (many solutions; the engine picks arbitrarily) |
| solver | E-S3 | Instability (a small change produces a different solution) |
| solver | E-S4 | Objective mis-specified (solves the wrong problem well) |
| planner | E-P1 | Plan-dependent semantics (the result depends on the chosen plan) |
| planner | E-P2 | Partial-value logic surprise (null, missing, three-valued) |
| reconciler | E-Re1 | Non-convergence |
| reconciler | E-Re2 | Oscillation |
| reconciler | E-Re3 | Drift (an external change is not reconciled) |
| reconciler | E-Re4 | Destructive reconcile (replace where update was intended) |
| lowering | E-L1 | Unfaithful lowering (the substrate result differs from the denotation) |
| lowering | E-L2 | Dead or unreachable declarations accepted silently |
| lowering | E-L3 | Target divergence (same description, different behaviour per substrate or version) |
| dataflow | E-D1 | Glitch (an observable inconsistent intermediate state) |
| dataflow | E-D2 | Stale dependency (a missing edge; not recomputed) — `seam` |
| dataflow | E-D3 | Unbounded propagation (cycle or infinite update) |
| templating | E-T1 | Escaping or injection (substituted text changes structure) |
| templating | E-T2 | Partial expansion (a placeholder survives into the output) |

### Mutant procedure (measured mode)

For each live class: take a valid, oracle-passing intent-corpus program tagged with the class;
apply the smallest change that instantiates the class; run it through the declared toolchain up
to and past the ship boundary; record the first stage with a signal, or `silent` with what the
program did instead. For `deleted`, attempt the mutant and record why the surface cannot express
it. Keep every mutant under the evidence path named on the card.

## Appendix B — Migration from v2

All v2 cards are invalid under v3 and must be re-scored. Field map:

| v2 | v3 |
|---|---|
| Litmus 0–8 total, four or five checks | Three checks, no total (A.3); say-the-delta → R7 |
| Δ.1 example ladder 0–5 | (L, S, T) vector 0–6 plus ρ (B.1) |
| Δ.2 system-anchored ladder 0–5 | Derivation-class ladder 0–5 (B.2) |
| Δ = (Δ.1 + Δ.2) / 2 | Never averaged; position is the triple |
| Histogram `deleted static runtime silent` (undefined population) | RET partition per class; stages `deleted decode validate load first-run latent silent`, `absent` excluded (B.3) |
| C bands (overlapping, `≤ 2` hole) | `C_cont` total function, `C_band` with caps (B.3.3); κ scored |
| Soundness / completeness "also record" | Downgrade rule; κ in C_cont |
| Quadrants and cutoffs | Dropped; frontier under floors (Part F) |
| Loss = distance from corner | Pareto dominance; scalar only with declared weights |
| Representational efficiency | R7, held-out, with delta-proportionality |
| Predictable compositionality | R3, measured as q = I/F |
| Composability (0–2) | Closure tie-breaker, unchanged |
| Operational adequacy (escape rate, coverage) | R4 containment plus R6 held-out coverage |
| Authorability-intrinsic (undefined) | Part E panel |
| Oracle-quality | R5 oracle independence; golden intent demoted to 2 |
| Design-stage "envelope intent" | Gate specifiability; C as an interval (B.3.4) |
| Temporality as prior | Kept; archetype selects E-classes (P4) |
| Unit of evaluation | Kept; coherence criteria added (A.1); seams scored (A.2, B.3.5) |
| (none) | R1 semantic definition, R2 explainability, D1–D3, Part G calibration |
