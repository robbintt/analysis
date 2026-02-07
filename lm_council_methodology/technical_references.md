# Technical References and Backlinks (ArXiv)

Date: 2026-02-06

This document provides end-to-end technical traceability from implementation claims to source papers, with direct backlinks to arXiv for every referenced claim in `method_claim_table.md`.

## Coverage

- Total extracted claims: **50**
- Total unique arXiv papers referenced by claims: **17**
- All claim rows below include direct arXiv links.

---

## A) Master bibliography (all papers used in claim extraction)

| arXiv ID | Paper | Link | Local digest file | Claim IDs linked |
|---|---|---|---|---|
| `2502.02533` | Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies | [arXiv abs](https://arxiv.org/abs/2502.02533) | `2502.02533_multi-agent-design-optimizing-agents-with-better-prompts-and-topologies_20260203_135543.md` | 17, 18, 19 |
| `2502.11133` | MasRouter: Learning to Route LLMs for Multi-Agent Systems | [arXiv abs](https://arxiv.org/abs/2502.11133) | `2502.11133_masrouter-learning-to-route-llms-for-multi-agent-systems_20260203_134336.md` | 24, 25, 26 |
| `2502.14815` | LiveCodeBenchCommonGenHardSimpleQA FEVER TableArithmetic TableBias0 | [arXiv abs](https://arxiv.org/abs/2502.14815) | `2502.14815_livecodebenchcommongenhardsimpleqa-fever-tablearithmetic-tablebias0_20260128_011541.md` | 33, 34 |
| `2502.20379` | Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers | [arXiv abs](https://arxiv.org/abs/2502.20379) | `2502.20379_multi-agent-verification-scaling-test-time-compute-with-multiple-verifiers_20260127_204016.md` | 27, 28, 29 |
| `2503.01935` | MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents | [arXiv abs](https://arxiv.org/abs/2503.01935) | `2503.01935_multiagentbench-evaluating-the-collaboration-and-competition-of-llm-agents_20260203_063300.md` | 47, 48 |
| `2505.18286` | Single-agent or Multi-agent Systems? Why Not Both? | [arXiv abs](https://arxiv.org/abs/2505.18286) | `2505.18286_single-agent-or-multi-agent-systems-why-not-both_20260201_215346.md` | 1, 2, 3, 4, 5 |
| `2506.12928` | Scaling Test-time Compute for LLM Agents | [arXiv abs](https://arxiv.org/abs/2506.12928) | `2506.12928_scaling-test-time-compute-for-llm-agents_20260126_191018.md` | 35, 36, 37, 38 |
| `2507.04105` | Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing | [arXiv abs](https://arxiv.org/abs/2507.04105) | `2507.04105_enhancing-robustness-of-llm-driven-multi-agent-systems-through-randomized-smoothing_20260203_070618.md` | 46 |
| `2509.20182` | Automated Multi-Agent Workflows for RTL Design | [arXiv abs](https://arxiv.org/abs/2509.20182) | `2509.20182_automated-multi-agent-workflows-for-rtl-design_20260203_122839.md` | 49, 50 |
| `2510.04311` | On the Importance of Task Complexity in Evaluating LLM-Based Multi-Agent Systems | [arXiv abs](https://arxiv.org/abs/2510.04311) | `2510.04311_on-the-importance-of-task-complexity-in-evaluating-llm-based-multi-agent-systems_20260127_211032.md` | 14, 15, 16 |
| `2511.01805` | Accumulating Context Changes the Beliefs of Language Models | [arXiv abs](https://arxiv.org/abs/2511.01805) | `2511.01805_accumulating-context-changes-the-beliefs-of-language-models_20260203_123127.md` | 41, 42 |
| `2511.10949` | Exposing Weak Links in Multi-Agent Systems under Adversarial Prompting | [arXiv abs](https://arxiv.org/abs/2511.10949) | `2511.10949_exposing-weak-links-in-multi-agent-systems-under-adversarial-prompting_20260203_122637.md` | 43, 44, 45 |
| `2511.15738` | Extending Test-Time Scaling: A 3D Perspective with Context, Batch, and Turn | [arXiv abs](https://arxiv.org/abs/2511.15738) | `2511.15738_extending-test-time-scaling-a-3d-perspective-with-context-batch-and-turn_20260126_190700.md` | 30, 31, 32 |
| `2511.22854` | CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate | [arXiv abs](https://arxiv.org/abs/2511.22854) | `2511.22854_crawdad-causal-reasoning-augmentation-with-dual-agent-debate_20260203_065941.md` | 20, 21, 22, 23 |
| `2512.08296` | Towards a Science of Scaling Agent Systems | [arXiv abs](https://arxiv.org/abs/2512.08296) | `2512.08296_towards-a-science-of-scaling-agent-systems_20260203_050314.md` | 9, 10, 11, 12, 13 |
| `2601.10560` | Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems | [arXiv abs](https://arxiv.org/abs/2601.10560) | `2601.10560_learning-latency-aware-orchestration-for-parallel-multi-agent-systems_20260203_130424.md` | 39, 40 |
| `2601.12307` | Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline | [arXiv abs](https://arxiv.org/abs/2601.12307) | `2601.12307_rethinking-the-value-of-multi-agent-workflow-a-strong-single-agent-baseline_20260203_134351.md` | 6, 7, 8 |

---

## B) Claim-level technical backlinks

| Claim ID | Verdict | Claim (short) | Boundary/condition | ArXiv backlinks | Confidence |
|---:|---|---|---|---|---|
| 1 | DONT | Use static MAS by default on frontier models. | Frontier SAS already strong. | [`2505.18286`](https://arxiv.org/abs/2505.18286) | High |
| 2 | DONT | Accept large MAS overhead for tiny gains. | MAS gain can be 0.8–3% for 5–220× token cost. | [`2505.18286`](https://arxiv.org/abs/2505.18286) | High |
| 3 | DONT | Assume MAS always beats SAS. | ~80% ties; SAS sometimes wins. | [`2505.18286`](https://arxiv.org/abs/2505.18286) | High |
| 4 | DO | Use request cascading (SAS↔MAS) rather than pure SAS or pure MAS. | Route by complexity/error profile. | [`2505.18286`](https://arxiv.org/abs/2505.18286) | High |
| 5 | DO | Apply MAS selectively to high-value subtasks only. | Only where error profile justifies premium. | [`2505.18286`](https://arxiv.org/abs/2505.18286) | High |
| 6 | DONT | Assume homogeneous MAS is necessary. | Homogeneous MAS can be simulated by one agent. | [`2601.12307`](https://arxiv.org/abs/2601.12307) | High |
| 7 | DO | Reuse KV cache and unified history for homogeneous-role simulation. | Same base model workflows. | [`2601.12307`](https://arxiv.org/abs/2601.12307) | High |
| 8 | MIXED | Single-agent simulation has limits for true heterogeneity. | Different base LLMs break cache sharing. | [`2601.12307`](https://arxiv.org/abs/2601.12307) | High |
| 9 | DO | Prefer heterogeneous teams when capability mix matters. | Low orchestrator + high sub-agents can win. | [`2512.08296`](https://arxiv.org/abs/2512.08296) | High |
| 10 | DO | Prioritize sub-agent quality over orchestrator quality. | Sub-agent bottleneck dominates. | [`2512.08296`](https://arxiv.org/abs/2512.08296) | High |
| 11 | DO | Keep coordination overhead in an optimal band. | Best around 200%–300%. | [`2512.08296`](https://arxiv.org/abs/2512.08296) | High |
| 12 | DONT | Over-coordinate with complex protocols. | >400% overhead reduces efficiency and raises failures. | [`2512.08296`](https://arxiv.org/abs/2512.08296) | High |
| 13 | DONT | Assume hybrid is safest architecture. | Hybrid had highest coordination failure (12.4%). | [`2512.08296`](https://arxiv.org/abs/2512.08296) | High |
| 14 | DO | Use debate-heavy MAS for deep sequential reasoning tasks. | High depth tasks. | [`2510.04311`](https://arxiv.org/abs/2510.04311) | Medium |
| 15 | DONT | Spend debate overhead on width-heavy/low-depth tasks. | Width gains saturate; cost may dominate. | [`2510.04311`](https://arxiv.org/abs/2510.04311) | High |
| 16 | DO | Treat depth and width separately in method selection. | Depth drives gains more than width. | [`2510.04311`](https://arxiv.org/abs/2510.04311) | Medium |
| 17 | DO | Jointly optimize prompts and topology (interleaved). | Manual/isolated tuning is suboptimal. | [`2502.02533`](https://arxiv.org/abs/2502.02533) | High |
| 18 | DO | Use search over fixed topologies. | Beneficial topologies are sparse and task-specific. | [`2502.02533`](https://arxiv.org/abs/2502.02533) | High |
| 19 | DONT | Standardize on “debate topology” globally. | Debate only helped specific tasks in analysis. | [`2502.02533`](https://arxiv.org/abs/2502.02533) | High |
| 20 | DO | Use conditional, disagreement-triggered debate. | Debate only when agents disagree. | [`2511.22854`](https://arxiv.org/abs/2511.22854) | High |
| 21 | DO | Prefer judge-free dual debate when judge bias is concern. | Judge-free setup; consensus stop. | [`2511.22854`](https://arxiv.org/abs/2511.22854) | Medium |
| 22 | DO | Use dual-agent debate for counterfactual/causal tasks. | Large counterfactual gains observed. | [`2511.22854`](https://arxiv.org/abs/2511.22854) | High |
| 23 | DO | Track consensus rounds + response length as efficiency metrics. | For cost-quality management. | [`2511.22854`](https://arxiv.org/abs/2511.22854) | Medium |
| 24 | DO | Dynamically route topology/roles/models per query (MASR). | Task/query dependent routing. | [`2502.11133`](https://arxiv.org/abs/2502.11133) | High |
| 25 | DO | Optimize utility-cost objective explicitly for routing. | `max E[U - λC]`. | [`2502.11133`](https://arxiv.org/abs/2502.11133) | Medium |
| 26 | DO | Use dynamic router to cut overhead while raising quality. | MBPP +1.8–8.2%; HumanEval overhead -52.07%. | [`2502.11133`](https://arxiv.org/abs/2502.11133) | High |
| 27 | DO | Scale verifier count, not just candidate count, under fixed budget. | m=64,n=4 > m=4,n=64 at fixed compute. | [`2502.20379`](https://arxiv.org/abs/2502.20379) | High |
| 28 | DO | Replace RM-only selection with multi-verifier consensus when feasible. | BoN-MAV beat Self-Consistency and BoN-RM. | [`2502.20379`](https://arxiv.org/abs/2502.20379) | High |
| 29 | DO | Leverage weak-to-strong verifier ensembles. | 9 weak verifiers approximated stronger supervision. | [`2502.20379`](https://arxiv.org/abs/2502.20379) | Medium |
| 30 | DONT | Rely on context-window-only test-time scaling. | Single-dimension scaling has bounded capacity. | [`2511.15738`](https://arxiv.org/abs/2511.15738) | Medium |
| 31 | DO | Allocate compute across context+batch+turn jointly. | Integrated 3D scaling outperforms isolated scaling. | [`2511.15738`](https://arxiv.org/abs/2511.15738) | Medium |
| 32 | DO | Use explicit token-budget accounting for test-time methods. | Cost measured by theoretical max generated tokens. | [`2511.15738`](https://arxiv.org/abs/2511.15738) | Medium |
| 33 | DONT | Use one identical LLM across all workflow modules by default. | Uniform assignment often suboptimal. | [`2502.14815`](https://arxiv.org/abs/2502.14815) | High |
| 34 | DO | Perform module-wise model assignment in compound workflows. | 5%–70% improvements reported. | [`2502.14815`](https://arxiv.org/abs/2502.14815) | High |
| 35 | DO | Use threshold-triggered reflection instead of continuous reflection. | Continuous reflection had poor cost-benefit. | [`2506.12928`](https://arxiv.org/abs/2506.12928) | Medium |
| 36 | DO | Prefer list-wise verification/merging over voting/scoring in this setting. | Better accuracy per compute token. | [`2506.12928`](https://arxiv.org/abs/2506.12928) | Medium |
| 37 | DONT | Depend on naive Best-of-N scaling alone. | BoN showed diminishing returns. | [`2506.12928`](https://arxiv.org/abs/2506.12928) | Medium |
| 38 | DO | Increase rollout diversity for better success rates. | Positive correlation with task success. | [`2506.12928`](https://arxiv.org/abs/2506.12928) | Medium |
| 39 | DONT | Optimize parallel MAS with sequential-cost assumptions. | Sequential assumptions are latency-suboptimal. | [`2601.10560`](https://arxiv.org/abs/2601.10560) | High |
| 40 | DO | Optimize critical execution path for parallel agent systems. | 38–46% latency reduction, no quality loss. | [`2601.10560`](https://arxiv.org/abs/2601.10560) | High |
| 41 | DONT | Ignore long-horizon context drift in multi-round systems. | Belief/behavior drift under debate/reading. | [`2511.01805`](https://arxiv.org/abs/2511.01805) | High |
| 42 | DO | Add drift monitoring and post-context behavior checks. | Behavior can shift materially after context accumulation. | [`2511.01805`](https://arxiv.org/abs/2511.01805) | High |
| 43 | DONT | Treat single-agent security metrics as sufficient for MAS. | ASR/RR insufficient for failure localization. | [`2511.10949`](https://arxiv.org/abs/2511.10949) | High |
| 44 | DONT | Assume centralized atomic delegation is robust by default. | Can obscure harmful objectives and raise critical risk. | [`2511.10949`](https://arxiv.org/abs/2511.10949) | High |
| 45 | DO | Use fine-grained MAS risk taxonomies (e.g., ARIA levels). | Better severity differentiation than pass/fail. | [`2511.10949`](https://arxiv.org/abs/2511.10949) | Medium |
| 46 | DO | Add consensus-level robustness defenses in adversarial settings. | Randomized smoothing reduced deviation by 90.24%. | [`2507.04105`](https://arxiv.org/abs/2507.04105) | Medium |
| 47 | DO | Prefer graph coordination topology where collaboration quality matters. | Graph outperformed star/chain/tree. | [`2503.01935`](https://arxiv.org/abs/2503.01935) | Medium |
| 48 | DO | Use cognitive planning over plain group discussion for coordination benchmarks. | +3% milestone achievement. | [`2503.01935`](https://arxiv.org/abs/2503.01935) | Medium |
| 49 | DO | Use confidence-triggered operator escalation (cascade). | Dynamic cascade improved pass@k and cost vs heavy self-refine. | [`2509.20182`](https://arxiv.org/abs/2509.20182) | Medium |
| 50 | DONT | Default to expensive always-heavy operators (e.g., persistent Self-Refine). | Self-Refine cost multiplier much higher in reported setup. | [`2509.20182`](https://arxiv.org/abs/2509.20182) | Medium |

---

## C) Topic-indexed references (quick lookup)

### SAS vs MAS economics and routing

- `2505.18286` — [2505.18286_single-agent-or-multi-agent-systems-why-not-both_20260201_215346.md](https://arxiv.org/abs/2505.18286)  
  - Local digest: `2505.18286_single-agent-or-multi-agent-systems-why-not-both_20260201_215346.md`  
  - Linked claims: 1, 2, 3, 4, 5
- `2601.12307` — [Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline](https://arxiv.org/abs/2601.12307)  
  - Local digest: `2601.12307_rethinking-the-value-of-multi-agent-workflow-a-strong-single-agent-baseline_20260203_134351.md`  
  - Linked claims: 6, 7, 8
- `2502.11133` — [MasRouter: Learning to Route LLMs for Multi-Agent Systems](https://arxiv.org/abs/2502.11133)  
  - Local digest: `2502.11133_masrouter-learning-to-route-llms-for-multi-agent-systems_20260203_134336.md`  
  - Linked claims: 24, 25, 26

### Coordination regimes and architecture effects

- `2512.08296` — [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296)  
  - Local digest: `2512.08296_towards-a-science-of-scaling-agent-systems_20260203_050314.md`  
  - Linked claims: 9, 10, 11, 12, 13
- `2510.04311` — [On the Importance of Task Complexity in Evaluating LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2510.04311)  
  - Local digest: `2510.04311_on-the-importance-of-task-complexity-in-evaluating-llm-based-multi-agent-systems_20260127_211032.md`  
  - Linked claims: 14, 15, 16

### Debate protocol design

- `2511.22854` — [CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate](https://arxiv.org/abs/2511.22854)  
  - Local digest: `2511.22854_crawdad-causal-reasoning-augmentation-with-dual-agent-debate_20260203_065941.md`  
  - Linked claims: 20, 21, 22, 23
- `2502.02533` — [Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies](https://arxiv.org/abs/2502.02533)  
  - Local digest: `2502.02533_multi-agent-design-optimizing-agents-with-better-prompts-and-topologies_20260203_135543.md`  
  - Linked claims: 17, 18, 19

### Verification and selection

- `2502.20379` — [Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers](https://arxiv.org/abs/2502.20379)  
  - Local digest: `2502.20379_multi-agent-verification-scaling-test-time-compute-with-multiple-verifiers_20260127_204016.md`  
  - Linked claims: 27, 28, 29
- `2506.12928` — [Scaling Test-time Compute for LLM Agents](https://arxiv.org/abs/2506.12928)  
  - Local digest: `2506.12928_scaling-test-time-compute-for-llm-agents_20260126_191018.md`  
  - Linked claims: 35, 36, 37, 38

### Compute scaling and allocation

- `2511.15738` — [Extending Test-Time Scaling: A 3D Perspective with Context, Batch, and Turn](https://arxiv.org/abs/2511.15738)  
  - Local digest: `2511.15738_extending-test-time-scaling-a-3d-perspective-with-context-batch-and-turn_20260126_190700.md`  
  - Linked claims: 30, 31, 32
- `2506.12928` — [Scaling Test-time Compute for LLM Agents](https://arxiv.org/abs/2506.12928)  
  - Local digest: `2506.12928_scaling-test-time-compute-for-llm-agents_20260126_191018.md`  
  - Linked claims: 35, 36, 37, 38

### Latency-aware orchestration

- `2601.10560` — [Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems](https://arxiv.org/abs/2601.10560)  
  - Local digest: `2601.10560_learning-latency-aware-orchestration-for-parallel-multi-agent-systems_20260203_130424.md`  
  - Linked claims: 39, 40

### Module/model assignment

- `2502.14815` — [LiveCodeBenchCommonGenHardSimpleQA FEVER TableArithmetic TableBias0](https://arxiv.org/abs/2502.14815)  
  - Local digest: `2502.14815_livecodebenchcommongenhardsimpleqa-fever-tablearithmetic-tablebias0_20260128_011541.md`  
  - Linked claims: 33, 34

### Security, robustness, drift

- `2511.10949` — [Exposing Weak Links in Multi-Agent Systems under Adversarial Prompting](https://arxiv.org/abs/2511.10949)  
  - Local digest: `2511.10949_exposing-weak-links-in-multi-agent-systems-under-adversarial-prompting_20260203_122637.md`  
  - Linked claims: 43, 44, 45
- `2507.04105` — [Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing](https://arxiv.org/abs/2507.04105)  
  - Local digest: `2507.04105_enhancing-robustness-of-llm-driven-multi-agent-systems-through-randomized-smoothing_20260203_070618.md`  
  - Linked claims: 46
- `2511.01805` — [Accumulating Context Changes the Beliefs of Language Models](https://arxiv.org/abs/2511.01805)  
  - Local digest: `2511.01805_accumulating-context-changes-the-beliefs-of-language-models_20260203_123127.md`  
  - Linked claims: 41, 42

### Evaluation substrate for coordination quality

- `2503.01935` — [MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents](https://arxiv.org/abs/2503.01935)  
  - Local digest: `2503.01935_multiagentbench-evaluating-the-collaboration-and-competition-of-llm-agents_20260203_063300.md`  
  - Linked claims: 47, 48

### Adaptive cascading workflows

- `2509.20182` — [Automated Multi-Agent Workflows for RTL Design](https://arxiv.org/abs/2509.20182)  
  - Local digest: `2509.20182_automated-multi-agent-workflows-for-rtl-design_20260203_122839.md`  
  - Linked claims: 49, 50

---

## D) Notes

- Backlinks use canonical arXiv abstract pages (`https://arxiv.org/abs/<id>`).
- Claim semantics are defined in `method_claim_table.md`; this file is strictly for reference traceability.
- If claims are revised, regenerate this document to maintain one-to-one traceability.
---

## E) Supplemental references cited in narrative documents (not claim-linked)

The following papers are cited in planning/synthesis narratives but are not currently linked to specific rows in `method_claim_table.md`.

| arXiv ID | Paper | Link | Local digest file | Referenced in docs |
|---|---|---|---|---|
| `2502.04506` | When One LLM Drools, Multi-LLM Collaboration Rules | [arXiv abs](https://arxiv.org/abs/2502.04506) | `2502.04506_when-one-llm-drools-multi-llm-collaboration-rules_20260127_210517.md` | `lm_council_bmad_corpus_report.md` |
| `2506.15451` | AgentGroupChat-V2: Divide-and-Conquer Is What LLM-Based Multi-Agent System | [arXiv abs](https://arxiv.org/abs/2506.15451) | `2506.15451_agentgroupchat-v2-divide-and-conquer-is-what-llm-based-multi-agent-system-need_20260203_134221.md` | `lm_council_bmad_corpus_report.md` |
| `2507.21028` | Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional | [arXiv abs](https://arxiv.org/abs/2507.21028) | `2507.21028_multi-agent-as-judge-aligning-llm-agent-based-automated-evaluation-with-multi-dimensional-human-evaluation_20260128_010338.md` | `lm_council_bmad_corpus_report.md` |
