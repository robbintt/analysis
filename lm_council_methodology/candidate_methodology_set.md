# Candidate Methodology Set (Round A)

Date: 2026-02-06  
Objective: prioritize papers that maximize extraction of **what works / what fails / boundary conditions** for LM-council-style systems.

## Selection Logic
Included when paper has:
1. explicit comparative outcomes (improvement + cost/latency/overhead),
2. concrete mechanism (debate/routing/topology/verification/orchestration),
3. boundary conditions (thresholds, regimes, diminishing returns),
4. reproducible methodology signal (benchmark + baselines).

Excluded for now: papers primarily about quantization, MoE internals, or non-agent domains without transferable orchestration evidence.

---

## Ranked shortlist (failure-first extraction value)

| Rank | File | Why high-value for Do/Don’t extraction |
|---:|---|---|
| 1 | `2505.18286_single-agent-or-multi-agent-systems-why-not-both_20260201_215346.md` | Strong negative evidence: MAS gains can collapse on frontier models while token costs explode; proposes request cascading (SAS↔MAS) as corrective. |
| 2 | `2601.12307_rethinking-the-value-of-multi-agent-workflow-a-strong-single-agent-baseline_20260203_134351.md` | Critical counterfactual: homogeneous MAS can be simulated by strong single-agent workflow with lower cost; prevents over-claiming MAS benefit. |
| 3 | `2512.08296_towards-a-science-of-scaling-agent-systems_20260203_050314.md` | Quantitative operating regime: optimal coordination band vs over-coordination failure; heterogeneity and sub-agent bottleneck evidence. |
| 4 | `2510.04311_on-the-importance-of-task-complexity-in-evaluating-llm-based-multi-agent-systems_20260127_211032.md` | Boundary model: depth vs width explains when debate overhead is justified vs wasteful. |
| 5 | `2601.14652_mas-orchestra-understanding-and-improving-multi-agent-reasoning-through-holistic-orchestration-and-controlled-benchmarks_20260203_133924.md` | “Conditional MAS utility” framing + edge-of-competence regime + controlled benchmark dimensions. |
| 6 | `2502.02533_multi-agent-design-optimizing-agents-with-better-prompts-and-topologies_20260203_135543.md` | Topology sparsity result: fixed topology often wrong; supports search-based design and rejects one-size-fits-all debate. |
| 7 | `2502.04506_when-one-llm-drools-multi-llm-collaboration-rules_20260127_210517.md` | Mechanistic evidence for iterative critique+refine outperforming vote-only; explicit cost/latency tradeoff. |
| 8 | `2511.22854_crawdad-causal-reasoning-augmentation-with-dual-agent-debate_20260203_065941.md` | High-value pattern: disagreement-triggered, judge-free conditional debate with consensus stopping. |
| 9 | `2502.11133_masrouter-learning-to-route-llms-for-multi-agent-systems_20260203_134336.md` | Dynamic routing across topology/roles/model backbones; strong cost reduction + performance gains. |
| 10 | `2502.20379_multi-agent-verification-scaling-test-time-compute-with-multiple-verifiers_20260127_204016.md` | Verification scaling law: verifier density can beat candidate-count scaling under fixed compute. |
| 11 | `2511.15738_extending-test-time-scaling-a-3d-perspective-with-context-batch-and-turn_20260126_190700.md` | Rejects context-only scaling; introduces context+batch+turn allocation frame. |
| 12 | `2502.14815_livecodebenchcommongenhardsimpleqa-fever-tablearithmetic-tablebias0_20260128_011541.md` | Anti-pattern evidence: uniform model assignment across modules is often suboptimal. |
| 13 | `2506.12928_scaling-test-time-compute-for-llm-agents_20260126_191018.md` | Practical inference tactics: thresholded reflection and list-wise verification outperform naive alternatives. |
| 14 | `2506.15451_agentgroupchat-v2-divide-and-conquer-is-what-llm-based-multi-agent-system-need_20260203_134221.md` | Width/depth tuning signal (rounds matter); useful for extracting decomposition and parallelism rules. |
| 15 | `2509.19236_agentinit-initializing-llm-based-multi-agent-systems-via-diversity-and-expertise-orchestration-for-effective-and-efficient-collaboration_20260203_063923.md` | Team initialization methodology: relevance/diversity Pareto selection to reduce redundancy and token waste. |
| 16 | `2601.10560_learning-latency-aware-orchestration-for-parallel-multi-agent-systems_20260203_130424.md` | Latency-first orchestration: optimize critical path, not total cost proxy; high practical deployment value. |
| 17 | `2511.10949_exposing-weak-links-in-multi-agent-systems-under-adversarial-prompting_20260203_122637.md` | Failure localization under adversarial prompting; identifies architecture-specific weak links. |
| 18 | `2507.04105_enhancing-robustness-of-llm-driven-multi-agent-systems-through-randomized-smoothing_20260203_070618.md` | Robustness method with quantified stability gains in safety-critical multi-agent consensus. |
| 19 | `2509.20182_automated-multi-agent-workflows-for-rtl-design_20260203_122839.md` | Dynamic cascading controller with confidence-triggered operator escalation; useful adaptive-control pattern. |
| 20 | `2503.01935_multiagentbench-evaluating-the-collaboration-and-competition-of-llm-agents_20260203_063300.md` | Evaluation substrate for coordination quality (topology + planning effects), not just final accuracy. |
| 21 | `2507.21028_multi-agent-as-judge-aligning-llm-agent-based-automated-evaluation-with-multi-dimensional-human-evaluation_20260128_010338.md` | In-group debate + aggregation workflow; useful for judge/aggregator protocol extraction. |
| 22 | `2511.01805_accumulating-context-changes-the-beliefs-of-language-models_20260203_123127.md` | Long-horizon risk evidence: context-induced drift; must inform context policy and rounds/memory controls. |
| 23 | `2512.08743_single-agent-scaling-fails-multi-agent-intelligence-towards-foundation-models-with-native-multi-agent-intelligence_20260203_065143.md` | Macro-level caution: single-agent scaling does not reliably transfer to multi-agent planning/coordination. |
| 24 | `2504.01963_llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems_20260203_124709.md` | Survey synthesis for architecture/memory/planning/framework bottlenecks; broad triangulation support. |

---

## Extraction order (to maximize outcome gains quickly)

### Wave 1 (Immediate impact on design choices)
`#1, #2, #3, #4, #6, #8, #9, #10`

Focus questions:
- When should MAS be avoided entirely?
- What are hard thresholds (overhead, base-model capability) for switching to SAS?
- Which debate patterns are cost-effective (conditional vs always-on)?
- What routing/topology adaptations create biggest quality-per-cost gains?

### Wave 2 (Operational optimization)
`#11, #12, #13, #14, #15, #16`

Focus questions:
- How to allocate test-time compute across context/batch/turn/verification?
- How to select models/roles/teams without brute force?
- How to optimize for wall-clock latency, not just token count?

### Wave 3 (Robustness + evaluation hardening)
`#17, #18, #19, #20, #21, #22, #23, #24`

Focus questions:
- Which architectures fail under attack/prompt injection?
- How to monitor and mitigate long-horizon drift?
- Which benchmark metrics detect coordination quality vs superficial success?

---

## Expected output from this candidate set
- >=20 failure/fragility claims with boundary conditions
- >=15 conditional “use X only when Y” rules
- Do/Don’t matrix with confidence labels (High/Medium/Low)
- Pre-run decision checklist for method selection before expensive experiments
