# Method Claim Table (Round B, Failure-First)

Date: 2026-02-06

Legend:
- **Verdict**: DO / DONT / MIXED
- **Confidence**: High (quant + baseline + boundary), Medium (quant partial), Low (descriptive)

| ID | Verdict | Methodology claim | Boundary / condition | Evidence anchors | Confidence |
|---:|---|---|---|---|---|
| 1 | DONT | Use static MAS by default on frontier models. | Frontier SAS already strong. | `2505.18286:20,22,147-148` | High |
| 2 | DONT | Accept large MAS overhead for tiny gains. | MAS gain can be 0.8–3% for 5–220× token cost. | `2505.18286:22,148` | High |
| 3 | DONT | Assume MAS always beats SAS. | ~80% ties; SAS sometimes wins. | `2505.18286:141-143` | High |
| 4 | DO | Use request cascading (SAS↔MAS) rather than pure SAS or pure MAS. | Route by complexity/error profile. | `2505.18286:24,40,165` | High |
| 5 | DO | Apply MAS selectively to high-value subtasks only. | Only where error profile justifies premium. | `2505.18286:174` | High |
| 6 | DONT | Assume homogeneous MAS is necessary. | Homogeneous MAS can be simulated by one agent. | `2601.12307:45,47,96,112` | High |
| 7 | DO | Reuse KV cache and unified history for homogeneous-role simulation. | Same base model workflows. | `2601.12307:47,80,97` | High |
| 8 | MIXED | Single-agent simulation has limits for true heterogeneity. | Different base LLMs break cache sharing. | `2601.12307:58,98,114` | High |
| 9 | DO | Prefer heterogeneous teams when capability mix matters. | Low orchestrator + high sub-agents can win. | `2512.08296:48,56,99` | High |
| 10 | DO | Prioritize sub-agent quality over orchestrator quality. | Sub-agent bottleneck dominates. | `2512.08296:57` | High |
| 11 | DO | Keep coordination overhead in an optimal band. | Best around 200%–300%. | `2512.08296:50,58,124` | High |
| 12 | DONT | Over-coordinate with complex protocols. | >400% overhead reduces efficiency and raises failures. | `2512.08296:59,125` | High |
| 13 | DONT | Assume hybrid is safest architecture. | Hybrid had highest coordination failure (12.4%). | `2512.08296:116` | High |
| 14 | DO | Use debate-heavy MAS for deep sequential reasoning tasks. | High depth tasks. | `2510.04311:47,104` | Medium |
| 15 | DONT | Spend debate overhead on width-heavy/low-depth tasks. | Width gains saturate; cost may dominate. | `2510.04311:47,105` | High |
| 16 | DO | Treat depth and width separately in method selection. | Depth drives gains more than width. | `2510.04311:45,56-57,104-106` | Medium |
| 17 | DO | Jointly optimize prompts and topology (interleaved). | Manual/isolated tuning is suboptimal. | `2502.02533:45,50-51,55` | High |
| 18 | DO | Use search over fixed topologies. | Beneficial topologies are sparse and task-specific. | `2502.02533:55,116` | High |
| 19 | DONT | Standardize on “debate topology” globally. | Debate only helped specific tasks in analysis. | `2502.02533:116` | High |
| 20 | DO | Use conditional, disagreement-triggered debate. | Debate only when agents disagree. | `2511.22854:51,88` | High |
| 21 | DO | Prefer judge-free dual debate when judge bias is concern. | Judge-free setup; consensus stop. | `2511.22854:40,51,88` | Medium |
| 22 | DO | Use dual-agent debate for counterfactual/causal tasks. | Large counterfactual gains observed. | `2511.22854:59-60,106,108` | High |
| 23 | DO | Track consensus rounds + response length as efficiency metrics. | For cost-quality management. | `2511.22854:114` | Medium |
| 24 | DO | Dynamically route topology/roles/models per query (MASR). | Task/query dependent routing. | `2502.11133:47,50-53,55` | High |
| 25 | DO | Optimize utility-cost objective explicitly for routing. | `max E[U - λC]`. | `2502.11133:55,106-107` | Medium |
| 26 | DO | Use dynamic router to cut overhead while raising quality. | MBPP +1.8–8.2%; HumanEval overhead -52.07%. | `2502.11133:36-38,59-61,129-131` | High |
| 27 | DO | Scale verifier count, not just candidate count, under fixed budget. | m=64,n=4 > m=4,n=64 at fixed compute. | `2502.20379:47` | High |
| 28 | DO | Replace RM-only selection with multi-verifier consensus when feasible. | BoN-MAV beat Self-Consistency and BoN-RM. | `2502.20379:47,101-102` | High |
| 29 | DO | Leverage weak-to-strong verifier ensembles. | 9 weak verifiers approximated stronger supervision. | `2502.20379:47,58,106` | Medium |
| 30 | DONT | Rely on context-window-only test-time scaling. | Single-dimension scaling has bounded capacity. | `2511.15738:42,54` | Medium |
| 31 | DO | Allocate compute across context+batch+turn jointly. | Integrated 3D scaling outperforms isolated scaling. | `2511.15738:44,55,116` | Medium |
| 32 | DO | Use explicit token-budget accounting for test-time methods. | Cost measured by theoretical max generated tokens. | `2511.15738:44,88` | Medium |
| 33 | DONT | Use one identical LLM across all workflow modules by default. | Uniform assignment often suboptimal. | `2502.14815:43,47,56,93-95` | High |
| 34 | DO | Perform module-wise model assignment in compound workflows. | 5%–70% improvements reported. | `2502.14815:33,47,56,94` | High |
| 35 | DO | Use threshold-triggered reflection instead of continuous reflection. | Continuous reflection had poor cost-benefit. | `2506.12928:57,117` | Medium |
| 36 | DO | Prefer list-wise verification/merging over voting/scoring in this setting. | Better accuracy per compute token. | `2506.12928:33,56,69,118` | Medium |
| 37 | DONT | Depend on naive Best-of-N scaling alone. | BoN showed diminishing returns. | `2506.12928:53` | Medium |
| 38 | DO | Increase rollout diversity for better success rates. | Positive correlation with task success. | `2506.12928:58,119` | Medium |
| 39 | DONT | Optimize parallel MAS with sequential-cost assumptions. | Sequential assumptions are latency-suboptimal. | `2601.10560:44,58` | High |
| 40 | DO | Optimize critical execution path for parallel agent systems. | 38–46% latency reduction, no quality loss. | `2601.10560:35-36,46,48,99-100` | High |
| 41 | DONT | Ignore long-horizon context drift in multi-round systems. | Belief/behavior drift under debate/reading. | `2511.01805:45,55-56,108-113,123` | High |
| 42 | DO | Add drift monitoring and post-context behavior checks. | Behavior can shift materially after context accumulation. | `2511.01805:55,68,113,117` | High |
| 43 | DONT | Treat single-agent security metrics as sufficient for MAS. | ASR/RR insufficient for failure localization. | `2511.10949:44,101-102` | High |
| 44 | DONT | Assume centralized atomic delegation is robust by default. | Can obscure harmful objectives and raise critical risk. | `2511.10949:44,57-58` | High |
| 45 | DO | Use fine-grained MAS risk taxonomies (e.g., ARIA levels). | Better severity differentiation than pass/fail. | `2511.10949:46,105-110` | Medium |
| 46 | DO | Add consensus-level robustness defenses in adversarial settings. | Randomized smoothing reduced deviation by 90.24%. | `2507.04105:46,48,90` | Medium |
| 47 | DO | Prefer graph coordination topology where collaboration quality matters. | Graph outperformed star/chain/tree. | `2503.01935:37,50,60` | Medium |
| 48 | DO | Use cognitive planning over plain group discussion for coordination benchmarks. | +3% milestone achievement. | `2503.01935:38,51,61` | Medium |
| 49 | DO | Use confidence-triggered operator escalation (cascade). | Dynamic cascade improved pass@k and cost vs heavy self-refine. | `2509.20182:36,38,46,48,91,123-124` | Medium |
| 50 | DONT | Default to expensive always-heavy operators (e.g., persistent Self-Refine). | Self-Refine cost multiplier much higher in reported setup. | `2509.20182:48,123-124` | Medium |

---

## Immediate synthesis from the table

### High-confidence DONTs
1. Static MAS-by-default on frontier models.
2. Over-coordination beyond empirically useful overhead.
3. Homogeneous MAS assumptions without strong SAS baseline checks.
4. One-size-fits-all topology or vote-only aggregation.
5. Ignoring context drift and adversarial weak links.

### High-confidence DOs
1. SAS↔MAS dynamic routing.
2. Conditional debate (disagreement-triggered).
3. Joint prompt+topology optimization and dynamic model/role routing.
4. Critical-path optimization for parallel systems.
5. Verification-heavy test-time scaling and drift/security instrumentation.
