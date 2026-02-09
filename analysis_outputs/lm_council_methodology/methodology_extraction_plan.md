# Methodology Extraction Plan (Failure-First) for Better LM-Council Outcomes

Date: 2026-02-06

## Goal
Improve real-world outcomes (quality, reliability, cost) by extracting **actionable methodology rules** from the digest, with emphasis on:
1) what works,
2) what fails,
3) under which conditions each claim holds.

---

## Success Criteria
- Produce a **ranked Do/Don’t playbook** with evidence strength.
- Convert research claims into **testable gating rules** (when to use SAS, MAS, debate, voting, etc.).
- Reduce avoidable bad choices (e.g., over-coordination, static MAS) before experimentation.

Primary KPIs:
- % of recommendations with direct quantitative support (target: >80%)
- # of “negative findings” captured (target: >=20)
- # of conditional rules with explicit boundary conditions (target: >=15)

---

## Extraction Strategy (4 Rounds)

## Round A — Corpus Narrowing (High Signal)
Create a candidate set focused on methodological evidence, not general MAS discussion.

### Include papers that contain:
- comparative language: `outperform`, `underperform`, `diminishing`, `saturate`, `failure`, `overhead`, `cost`, `latency`
- mechanism language: `debate`, `critic`, `aggregator`, `voting`, `consensus`, `routing`, `topology`, `rounds`, `turns`
- boundary language: `only if`, `when`, `threshold`, `optimal band`, `collapse`

### Priority weighting:
- Higher `quality_score`
- Non-trivial `citation_count`
- Presence of explicit baselines + numeric deltas

Deliverable: `candidate_methodology_set.md` (ranked list + reason for inclusion)

---

## Round B — Structured Claim Extraction (Failure-First)
For each paper, extract into a normalized record:

- **Method** (e.g., conditional dual-agent debate)
- **Outcome** (works / fails / mixed)
- **Task regime** (high-depth math, low-depth QA, etc.)
- **Metric delta** (accuracy/F1/etc.)
- **Cost delta** (tokens/latency/overhead)
- **Failure mode** (coordination failure, drift, saturation)
- **Boundary condition** (e.g., overhead > 400%, frontier SAS accuracy > 90%)
- **Evidence strength** (High/Med/Low)
- **Citation anchors** (file:line)

Bias rule: capture **negative and null** findings before positive findings.

Deliverable: `method_claim_table.csv` (or md table)

---

## Round C — Cross-Paper Synthesis (Resolve Contradictions)
Aggregate claims into methodology families and identify moderators.

### Families
- Debate protocols (always-on vs disagreement-triggered)
- Aggregation (vote-only vs critique+refine+aggregate)
- Topology (fixed vs searched)
- Team composition (homogeneous vs heterogeneous)
- Orchestration intensity (under/optimal/over-coordination)
- Routing (static MAS vs SAS↔MAS cascading)
- Context governance (long-horizon drift controls)

### Output structure per family
- **Do** (with conditions)
- **Don’t** (with failure signatures)
- **Unknowns** (where evidence conflicts)

Deliverable: `methodology_do_dont_matrix.md`

---

## Round D — Convert to Decision Rules
Translate synthesis into operational decision rules:

Examples:
- If base SAS performance is high and marginal MAS gain < threshold, default SAS.
- Trigger debate only on disagreement/high uncertainty.
- Keep coordination overhead within empirically supported band.
- Require drift checks in long-horizon contexts.

Deliverable: `decision_rules_checklist.md` (pre-run checklist for your schema)

---

## Evidence Quality Rubric
Each claim gets a confidence score:
- **High**: direct quantitative comparison + baseline + cost tradeoff + clear boundary
- **Medium**: quantitative but partial cost/boundary detail
- **Low**: descriptive/no clear ablation

Prefer conservative rules when evidence is mixed.

---

## Immediate Next Actions (Fast, Practical)
1. Build candidate set of ~30 methodology-heavy papers from digest.
2. Extract at least 20 failure/fragility claims first.
3. Build a first Do/Don’t matrix with confidence labels.
4. Use matrix to select 3–5 methods for controlled testing.

---

## Known High-Value Seeds Already Identified
- Static MAS diminishing returns / high token multipliers: `2505.18286...`
- Over-coordination failure band: `2512.08296...`
- Homogeneous MAS ≈ strong SAS baseline: `2601.12307...`
- Conditional disagreement-triggered debate: `2511.22854...`
- Topology sparsity / search over fixed design: `2502.02533...`
- Debate useful with depth, less so when overhead dominates: `2510.04311...`
- Context-induced drift risk in long sessions: `2511.01805...`

These should anchor the first synthesis pass.
