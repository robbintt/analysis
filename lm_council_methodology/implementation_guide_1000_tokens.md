# Implementation Guide (≈1000 tokens): Selective LM-Council System

## 1) Goal and operating principle
Implement an LM-council system that improves reliability on hard tasks **without** paying universal multi-agent cost. The guiding principle is:

1. **Default to Single-Agent System (SAS)** for most requests.
2. **Escalate to Multi-Agent System (MAS)** only when triggers indicate potential value.
3. Enforce hard **cost, latency, and safety guardrails**.

This is a deployment strategy, not a single prompt pattern.

---

## 2) Minimum prerequisites
Before implementation, ensure you have:

- A strong SAS baseline for your target tasks.
- Unified logging for: quality, token usage, wall-clock latency, rounds, disagreement events, consensus events, failure labels.
- At least one benchmark split by task complexity (easy/medium/hard).
- A safety evaluation pass (prompt injection + long-horizon drift checks).

If any of these are missing, instrument first.

---

## 3) System architecture (schema-agnostic)
Build six modules:

1. **Router**: decides SAS vs MAS and selects topology/roles/models.
2. **Deliberation Engine**: runs conditional debate (if escalated).
3. **Verifier Layer**: scores candidates using multi-verifier consensus.
4. **Compute Governor**: enforces token/round budgets.
5. **Latency Governor**: optimizes critical path in parallel workflows.
6. **Safety Governor**: drift probes + adversarial weak-link checks.

Data flow:
`Input -> Router -> (SAS path OR MAS path) -> Verifier -> Output -> Post-checks`

---

## 4) Routing policy (first implementation)
Start with deterministic routing rules, then learn policy later.

### Escalate from SAS to MAS if any trigger fires:
- Complexity score above threshold (deep multi-step dependency).
- Low confidence or high uncertainty in SAS output.
- Internal disagreement signal (e.g., 2 quick independent drafts diverge).
- High-stakes domain flag (safety, legal, finance, medical, security).

### Stay in SAS if:
- Task is low-depth and routine.
- SAS confidence is high and uncertainty is low.
- Cost budget is near limit.

Use a conservative policy at first: under-triggering is safer than over-triggering.

---

## 5) MAS deliberation protocol (recommended default)
Use **disagreement-triggered, bounded debate**.

### Roles
- Proposer
- Critic
- Synthesizer (or judge-free consensus if preferred)

### Loop
1. Independent proposal(s).
2. Critique only where disagreement exists.
3. Revision.
4. Early stop on consensus OR max-round hit.

### Hard controls
- `max_rounds` (e.g., 2–4 to start)
- `per_round_token_cap`
- `total_token_cap`
- `early_stop_on_consensus = true`

Do **not** run always-on debate on all tasks.

---

## 6) Verification and candidate selection
After SAS/MAS generation, use verifier-centric selection rather than vote-only.

### Recommended pattern
- Generate small candidate set.
- Run multiple aspect verifiers (logic, factuality, spec compliance, safety).
- Aggregate with list-wise or weighted consensus.

### Practical setup
- Start with 3–5 verifiers (different prompts/models if possible).
- Track verifier agreement and calibration drift.
- If disagreement among verifiers is high, either escalate one more controlled round or return “needs clarification.”

Avoid relying on a single scalar reward score alone for critical outputs.

---

## 7) Compute and latency governance

## Compute governor
Track and enforce:
- Input tokens
- Output tokens
- Reasoning tokens (if applicable)
- Tokens by phase (proposal/critique/revision/verification)

Use a 3D allocation mindset:
- context budget,
- batch/candidate budget,
- turn/round budget.

Do not spend all compute on just longer context windows.

## Latency governor
For parallel paths, optimize **critical execution path** (longest dependency chain), not only aggregate compute cost.

- Parallelize independent verifier calls.
- Delay expensive branches until routing confidence justifies them.
- Log stage-level latency, not just end-to-end latency.

---

## 8) Safety and robustness layer
Implement two always-on protections:

1. **Drift checks (long sessions)**
   - Periodic probe prompts for policy/behavior consistency.
   - Compare pre/post-session behavioral decisions, not just text tone.

2. **Weak-link diagnostics (MAS-specific)**
   - Label failures by planner/delegation/aggregation stage.
   - Run adversarial prompting tests against each stage.

If critical-risk patterns appear, downgrade to SAS-first safe mode while investigating.

---

## 9) Rollout plan (4 phases)

### Phase 0: Offline baseline
- Freeze SAS baseline.
- Record quality/cost/latency per task stratum.

### Phase 1: Shadow mode
- Run router + MAS in parallel, do not serve outputs.
- Compare uplift and overhead by trigger type.

### Phase 2: Guarded traffic slice
- Enable selective council for 5–10% traffic.
- Activate hard kill switches:
  - cost multiplier ceiling,
  - latency SLO breach ceiling,
  - safety regression threshold.

### Phase 3: Progressive scaling
- Increase traffic only where uplift is stable and ROI positive.
- Keep low-depth cohorts on SAS by default.

---

## 10) Acceptance criteria (go/no-go)
Ship only if all are true:

- Quality gain above pre-set minimum vs SAS baseline.
- Cost multiplier within budget envelope.
- Latency meets SLO for target tier.
- Coordination overhead not in known over-coordination regime.
- No critical safety regressions in drift/adversarial tests.

If any fail: rollback to SAS-first and retune routing/debate thresholds.

---

## 11) First five A/B tests (mandatory)
1. Static MAS vs SAS→MAS cascading.
2. Always-on debate vs disagreement-triggered debate.
3. Vote/scoring aggregation vs verifier-centric selection.
4. Context-only scaling vs context+batch+turn budgeting.
5. Aggregate-cost optimization vs critical-path latency optimization.

Treat these as gates before any broad production rollout.

---

## 12) Common implementation mistakes
- Routing too aggressively into MAS.
- No round caps (runaway token spend).
- Optimizing quality only, ignoring latency.
- Using one model across all modules without testing alternatives.
- Security evaluation limited to single-agent metrics.

---

## 13) Practical default profile (starter)
- SAS default: ON
- MAS escalation threshold: conservative
- Debate trigger: disagreement-only
- Max rounds: 3
- Early stop: consensus required
- Candidate count: small (e.g., 3–5)
- Verifiers: 3+
- Drift probes: periodic on long sessions
- Kill switch: strict on cost and latency

Use this as a safe initial posture, then specialize per domain.
