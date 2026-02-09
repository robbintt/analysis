# Decision Rules Checklist (Round D)

Date: 2026-02-06  
Purpose: operational rules you can map to your own schema before running expensive experiments.

## 0) Readiness gate (must pass)
- [ ] You have a **SAS baseline** on the same tasks.
- [ ] You can measure **quality + cost + latency** together.
- [ ] You log: rounds, disagreements, consensus stops, token usage, wall-clock, failure mode labels.

If any unchecked: stop and instrument first.

---

## 1) Architecture selection rules (SAS vs MAS)

### Rule A1 — Default posture
- Use **SAS-first** as default.
- Escalate to MAS only if one or more is true:
  - high task depth / multi-step dependency,
  - uncertainty/disagreement signal,
  - high-stakes verification need.

### Rule A2 — Frontier diminishing-returns guard
- If SAS baseline is already near high-accuracy regime (paper signal: ~90%), assume MAS gains may be marginal.
- Require projected gain threshold before MAS rollout; otherwise keep SAS.

### Rule A3 — Cost sanity guard
- If MAS cost multiplier is very high and quality lift is small, block rollout.
- Paper warning band: 0.8–3% gains at 5–220× token cost can happen.

---

## 2) Coordination intensity rules

### Rule C1 — Overhead band
- Target coordination overhead in **~200–300%** band (empirical sweet spot).
- If projected/observed overhead >400%, trigger redesign (likely over-coordination).

### Rule C2 — Hybrid caution
- Do not assume hybrid is safest by default; monitor coordination-failure rate explicitly.

---

## 3) Debate protocol rules

### Rule D1 — Trigger policy
- Use **disagreement-triggered debate**, not always-on debate.

### Rule D2 — Stop policy
- Require both:
  - max round cap,
  - early stop on consensus.

### Rule D3 — Task fit
- Prefer debate for high-depth / causal / counterfactual tasks.
- Avoid debate-heavy paths on low-depth or width-dominated tasks.

---

## 4) Topology and routing rules

### Rule T1 — No fixed global topology
- Do not lock one topology globally.
- Re-search/re-evaluate topology by task family.

### Rule T2 — Dynamic routing
- Route dynamically over topology + role + model selection.
- Optimize explicit utility-cost objective (quality minus weighted cost).

### Rule T3 — Homogeneous workflow check
- If all roles use same base model, test strong single-agent simulation baseline before keeping MAS decomposition.

---

## 5) Verification and selection rules

### Rule V1 — Verification-first for correctness-sensitive tasks
- Prefer multi-verifier consensus over single scalar RM where possible.

### Rule V2 — Compute allocation
- Under fixed compute, test scaling verifiers vs scaling candidates (not candidate count only).

### Rule V3 — Aggregation choice
- Prefer critique/refine + verifier selection over simple vote-only aggregation for hard reasoning tasks.

---

## 6) Test-time compute rules

### Rule X1 — Avoid one-axis scaling
- Do not rely on context-window expansion alone.
- Allocate compute across context + batch + turn.

### Rule X2 — Budget accounting
- Enforce token budgets at per-round and total-run levels.

### Rule X3 — Reflection policy
- Use threshold-triggered reflection.
- Avoid continuous reflection loops unless proven beneficial on your benchmark.

---

## 7) Module assignment rules (compound workflows)

### Rule M1 — Module-wise model assignment
- Do not use one identical model for every module by default.
- Run module-wise assignment search/heuristics first.

---

## 8) Latency rules (parallel systems)

### Rule L1 — Objective
- Optimize **critical execution path** for parallel workflows.
- Do not optimize only aggregate compute with sequential assumptions.

### Rule L2 — Acceptance
- Require latency win with no quality regression for production adoption.

---

## 9) Safety / robustness rules

### Rule S1 — Drift guard
- In long-horizon sessions, run periodic drift probes (belief/behavior consistency checks).

### Rule S2 — Security diagnostics
- Do not rely only on single-agent ASR/RR metrics.
- Use multi-agent failure taxonomy (planner/delegation/aggregation failure levels).

### Rule S3 — Adversarial environments
- Add robustness layer for consensus stability when threat model includes prompt attacks.

---

## 10) Go/No-Go rollout gate

Ship only if all are true:
- [ ] Quality gain clears your minimum bar vs SAS.
- [ ] Cost/latency are within budget envelope.
- [ ] Coordination overhead not in over-coordination regime.
- [ ] Debate/verification triggers are conditional (not always-on by default).
- [ ] Drift/security checks show no critical regressions.

If any fail: fallback to SAS-first or simplified MAS variant and retest.

---

## Minimal A/B set before production
1. Static MAS vs SAS↔MAS cascading
2. Always-on debate vs disagreement-triggered debate
3. Vote/scoring vs verifier-centric selection
4. Context-only scaling vs context+batch+turn budgeting
5. Aggregate-cost optimization vs critical-path optimization (parallel)
