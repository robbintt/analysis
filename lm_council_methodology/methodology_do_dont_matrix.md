# Methodology Do/Don’t Matrix (Round C)

Date: 2026-02-06  
Inputs: `method_claim_table.md` (IDs 1–50)

## 1) Contradictions resolved (cross-paper synthesis)

| Apparent conflict | Resolution | Evidence basis |
|---|---|---|
| “MAS helps” vs “MAS is not worth it” | **Both true conditionally**: MAS helps in high-depth/hard tasks, but static MAS under frontier models often has poor cost/benefit. | IDs 1,2,14,15 |
| “Single-agent is enough” vs “Need multiple agents” | **Homogeneous MAS** can often be simulated by single-agent; **heterogeneous/routed/verification-heavy** setups still add value. | IDs 6,8,9,24,27 |
| “Debate is good” vs “Debate is expensive” | Use **conditional disagreement-triggered debate** for targeted cases; avoid always-on debate. | IDs 15,20,22 |
| “More coordination is better” vs “coordination causes failures” | Coordination is non-linear: optimal band (~200–300% overhead), over-coordination (>400%) degrades outcomes. | IDs 11,12,13 |
| “Vote to aggregate” vs “deliberate to improve” | Vote-only is weaker in many settings; critique/refine + verifier consensus often superior. | IDs 19,28,36 |

---

## 2) Family-level Do/Don’t matrix

## A. System-level strategy (SAS vs MAS)
- **DO**: Start SAS-first, escalate to MAS only on complexity/uncertainty/error triggers.  
  - IDs: 4,5
- **DONT**: Deploy MAS universally on frontier stacks without ROI checks.  
  - IDs: 1,2,3
- **Condition**: If SAS baseline is already high (near threshold regime), MAS returns often collapse.
- **Confidence**: **High**

## B. Team composition
- **DO**: Prefer heterogeneous teams where role capability differs; prioritize strong sub-agents.  
  - IDs: 9,10
- **DONT**: Assume homogeneous decomposition adds value by default.  
  - IDs: 6,8
- **Condition**: Homogeneous same-backbone workflows are prime candidates for single-agent simulation.
- **Confidence**: **High**

## C. Debate and deliberation protocol
- **DO**: Use disagreement-triggered, conditional debate; stop on consensus/round caps.  
  - IDs: 20,22,23
- **DONT**: Use debate-heavy workflows for low-depth/width-dominated tasks.  
  - IDs: 15
- **Condition**: Debate value rises with depth/causal difficulty.
- **Confidence**: **High/Medium**

## D. Topology and orchestration
- **DO**: Search topology jointly with prompt optimization; rerun search per domain/task class.  
  - IDs: 17,18
- **DONT**: Hard-code one topology globally (including always “debate topology”).  
  - IDs: 19
- **Condition**: Useful topologies are sparse and task-dependent.
- **Confidence**: **High**

## E. Routing and adaptation
- **DO**: Route dynamically across topology, roles, and model backbones using utility-cost objective.  
  - IDs: 24,25,26
- **DONT**: Keep static model-role assignments for variable query difficulty.
- **Condition**: Dynamic routing offers strongest gains where query complexity is heterogeneous.
- **Confidence**: **High**

## F. Test-time compute allocation
- **DO**: Allocate compute across context+batch+turn; use explicit token budgets.  
  - IDs: 31,32
- **DONT**: Depend on context-window-only scaling or naive BoN-only scaling.  
  - IDs: 30,37
- **Condition**: Gains come from balanced multi-dimension compute, not one-axis scaling.
- **Confidence**: **Medium**

## G. Verification and selection
- **DO**: Use multi-verifier consensus; scale verifier density under fixed budget where beneficial.  
  - IDs: 27,28,29,36
- **DONT**: Rely solely on single RM or simple vote/scoring when verification quality is bottlenecked.
- **Condition**: Verification-heavy strategies are especially useful in reasoning correctness tasks.
- **Confidence**: **High/Medium**

## H. Module/model assignment in compound workflows
- **DO**: Optimize module-wise model assignment.  
  - IDs: 34
- **DONT**: Use a single identical model across all modules by default.  
  - IDs: 33
- **Condition**: Biggest gains when module competencies differ materially.
- **Confidence**: **High**

## I. Reflection and iterative correction
- **DO**: Trigger reflection conditionally (confidence-thresholded).  
  - IDs: 35
- **DONT**: Run continuous reflection loops indiscriminately.  
  - IDs: 35,50
- **Condition**: Continuous reflection often has poor cost-benefit.
- **Confidence**: **Medium**

## J. Latency optimization (parallel MAS)
- **DO**: Optimize critical execution path for parallel systems.  
  - IDs: 40
- **DONT**: Optimize only aggregate compute under sequential assumptions.  
  - IDs: 39
- **Condition**: Wall-clock-sensitive deployments require critical-path-aware orchestration.
- **Confidence**: **High**

## K. Robustness and security
- **DO**: Add drift monitoring and multi-agent risk taxonomy (ARIA-like) + adversarial robustness defenses.  
  - IDs: 42,45,46
- **DONT**: Treat single-agent safety metrics as sufficient, or assume centralized atomic delegation is safe.  
  - IDs: 41,43,44
- **Condition**: Long-horizon contexts and adversarial environments amplify systemic failures.
- **Confidence**: **High/Medium**

---

## 3) Recommended methodology stack (v1)

1. **SAS-first gate** with escalation triggers (difficulty/uncertainty/error).  
2. **Conditional debate** (disagreement-triggered) with round cap + consensus stop.  
3. **Dynamic routing** over topology/roles/models under explicit utility-cost objective.  
4. **Verifier-centric selection** (multi-verifier consensus; list-wise where applicable).  
5. **Compute governance** (context+batch+turn budgeting; avoid BoN-only inflation).  
6. **Latency governance** (critical-path objective in parallel workflows).  
7. **Safety governance** (drift checks, weak-link diagnostics, adversarial robustness layer).

---

## 4) What to test first (lowest-regret experiments)

1. **Routing A/B**: static MAS vs SAS↔MAS cascading.  
2. **Debate trigger A/B**: always-on vs disagreement-triggered.  
3. **Selection A/B**: vote/scoring vs multi-verifier list-wise consensus.  
4. **Compute A/B**: context-only scaling vs 3D budget (context+batch+turn).  
5. **Parallel latency A/B**: aggregate-cost objective vs critical-path objective.

These five tests directly validate the highest-confidence Do/Don’t claims and should quickly improve outcome-per-cost.
