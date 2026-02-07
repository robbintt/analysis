# LM Council / BMAD Corpus Scan Report

Date: 2026-02-06
Directory scanned: `.` (markdown summary corpus)

## Objective
Find occurrences of:
- `lm council` and close variants
- `bmad` (and likely formatting variants)

Then identify adjacent academic terms useful for configuration/method design with emphasis on rounds and context handling.

## Exact-Term Results

- `lm council | llm council | language model council | model council`: **0 hits**
- `bmad` and dotted variant (`b.m.a.d`): **0 hits**
- `MAD` as debate acronym: **1 relevant hit**
  - `2511.22854_crawdad-causal-reasoning-augmentation-with-dual-agent-debate_20260203_065941.md:81`

Note: plain word `council` appears once in an unrelated affiliation string.

## High-Signal Adjacent Terms (for methods/configs)

### 1) Multi-LLM round-table critique/refine
- File: `2502.04506_when-one-llm-drools-multi-llm-collaboration-rules_20260127_210517.md`
- Key lines:
  - `:46` multi-agent round-table discussion with 3 phases
  - `:76-80` iterative critique/debate -> answer refinement -> consensus aggregation
  - `:50, :60` explicit latency/cost trade-off

### 2) Judge-free conditional dual-agent debate (MAD)
- File: `2511.22854_crawdad-causal-reasoning-augmentation-with-dual-agent-debate_20260203_065941.md`
- Key lines:
  - `:40` core innovation: judge-free dual-agent debate
  - `:51` conditional debate only on disagreement; iterate until consensus
  - `:81` explicit label “Dual-Agent Debate paradigm (MAD)”
  - `:114` tracks consensus rounds required

### 3) Multi-turn debate with explicit aggregator agent
- File: `2510.04311_on-the-importance-of-task-complexity-in-evaluating-llm-based-multi-agent-systems_20260127_211032.md`
- Key lines:
  - `:45, :78` agents debate across multiple turns; aggregator synthesizes final answer
  - `:47` token overhead justified mostly for high-depth tasks

### 4) Architecture options + voting + cost overhead band
- File: `2512.08296_towards-a-science-of-scaling-agent-systems_20260203_050314.md`
- Key lines:
  - `:46` centralized / decentralized / hybrid / independent paradigms
  - `:72` decentralized = peer debate with voting
  - `:124` optimal coordination overhead band `200% < O < 300%`

### 5) In-group debate + aggregation workflow
- File: `2507.21028_multi-agent-as-judge-aligning-llm-agent-based-automated-evaluation-with-multi-dimensional-human-evaluation_20260128_010338.md`
- Key lines:
  - `:53` in-group debate before aggregation
  - `:99-102` debate & explicit aggregator agent

### 6) Workflow topology search (debate as one topology)
- File: `2502.02533_multi-agent-design-optimizing-agents-with-better-prompts-and-topologies_20260203_135543.md`
- Key lines:
  - `:50` topology optimization includes Aggregate / Reflect / Debate
  - `:99` fixed construction rule under budget constraint
  - `:116` topology sparsity; debate useful in specific tasks only

### 7) Frontier-cost warning for multi-agent deployments
- File: `2505.18286_single-agent-or-multi-agent-systems-why-not-both_20260201_215346.md`
- Key lines:
  - `:22` reports 5–220× token-cost overhead in some MAS settings
  - `:40` cascading MAS/SAS routing improves cost-accuracy balance
  - `:174` reserve MAS for subtasks where error profile justifies cost

### 8) Explicit context/batch/turn scaling formalism
- File: `2511.15738_extending-test-time-scaling-a-3d-perspective-with-context-batch-and-turn_20260126_190700.md`
- Key lines:
  - `:44` 3D test-time scaling: Context + Batch + Turn
  - `:78` context within token budget
  - `:86` iterative self-refinement across turns
  - `:88` compute cost measured by theoretical max generated tokens

## Practical Terminology to Use in Future Configs
- Multi-Agent Debate (MAD)
- Judge-free Dual-Agent Debate
- In-Group Debate + Aggregation
- Peer Debate with Voting
- Orchestrator–Subagent (centralized)
- Context / Batch / Turn scaling
- Coordination Overhead

## Bottom Line
The corpus does **not** use the exact labels “LM council” or “BMAD.”
Closest academic framing is **multi-agent debate / deliberation + aggregation/voting** with explicit **round, context, and cost** controls.

---

## Discovery Round 1 (Config/Method Extraction)

### Scope
Focused review of high-signal papers to extract implementation knobs for a practical "LM council" style configuration.

### Canonical protocol primitives found
1. **Independent proposal phase** before interaction
   - `2502.04506...:46`
2. **Iterative critique/debate phase**
   - `2502.04506...:46, :76`
   - `2511.22854...:51`
3. **Conditional debate trigger** (debate only on disagreement)
   - `2511.22854...:51, :88`
4. **Aggregation strategy** (aggregator agent or voting/consensus)
   - `2510.04311...:45, :78`
   - `2507.21028...:102`
   - `2512.08296...:72, :87`
5. **Turn/round control**
   - `2510.04311...:45` (multiple turns)
   - `2511.22854...:114` (consensus rounds tracked)
6. **Context/compute budgeting**
   - `2511.15738...:44, :78, :88` (context+batch+turn with token-budgeted compute)
7. **Topology search instead of fixed workflow**
   - `2502.02533...:50, :95-99, :116`
8. **Cost guardrails and dynamic routing**
   - `2512.08296...:58, :119` (coordination overhead)
   - `2505.18286...:24, :40, :147` (request cascading; MAS gains collapse in some frontier settings)
9. **Long-horizon context risk control**
   - `2511.01805...:45, :75, :123` (context-induced drift under accumulation)

### Recommended config dimensions for next step
- `roles`: proposer / critic / synthesizer (optional judge)
- `trigger_policy`: always-debate vs disagreement-only
- `max_rounds`: fixed cap, plus `early_stop_on_consensus`
- `context_policy`: full transcript vs rolling summary vs last-k turns
- `aggregation_policy`: aggregator model | majority vote | weighted vote
- `budget_policy`: token cap per round + total cap
- `topology_policy`: fixed template vs searched topology
- `routing_policy`: SAS-first, escalate to MAS on complexity/error signals
- `safety_policy`: drift checks across long sessions (belief/behavior consistency probes)

### Practical takeaway
For implementation, strongest evidence supports starting with:
- **Disagreement-triggered dual/multi-agent debate**,
- **Explicit round cap + consensus stop**,
- **Token/coordination budget guardrails**, and
- **Dynamic SAS↔MAS routing** for cost control.

---

## Discovery Round 2 (Methodologies: What Works vs Fails)

### Methods that tend to **work**

1. **Conditional debate (only on disagreement)**
   - Improves efficiency over always-on debate while preserving quality gains.
   - Refs: `2511.22854...:51, :88`

2. **Iterative critique -> refinement (not vote-only)**
   - Better reasoning/factuality than static majority voting in cited setups.
   - Refs: `2502.04506...:46, :58, :76-80`

3. **Heterogeneous teams + strong sub-agents**
   - Mixed-capability teams often beat homogeneous teams; sub-agent capability is key bottleneck.
   - Refs: `2512.08296...:48, :56-57`

4. **Coordination kept in an optimal band**
   - Best success/cost around 200%–300% coordination overhead.
   - Refs: `2512.08296...:58, :124`

5. **Dynamic SAS<->MAS routing (request cascading)**
   - Outperforms pure SAS or pure MAS in combined cost/accuracy.
   - Refs: `2505.18286...:24, :40`

6. **Joint optimization of prompts + topology**
   - Interleaved search outperforms manual/fixed design; useful topologies are task-dependent.
   - Refs: `2502.02533...:47, :50, :55`

7. **Module-specific model assignment in compound workflows**
   - Uniform model assignment is often inferior.
   - Refs: `2502.14815...:43, :47, :56`

8. **Parallel divide-and-conquer with tuned width/depth**
   - Gains on complex tasks when decomposition and rounds are tuned (not arbitrary).
   - Refs: `2506.15451...:47, :49, :83`

### Methods that often **do not work** (or are fragile)

1. **Static MAS-by-default on frontier models**
   - Marginal gains can collapse while token costs explode.
   - Refs: `2505.18286...:20, :22, :147-148`

2. **Over-coordination / protocol over-complexity**
   - Overhead >400% reduces efficiency and raises coordination failures.
   - Refs: `2512.08296...:50, :59, :125`

3. **Homogeneous multi-agent decomposition as a default assumption**
   - Strong single-agent simulation can match homogeneous MAS at lower cost.
   - Refs: `2601.12307...:47, :49, :80, :112-113`

4. **Fixed, hand-picked topologies across tasks**
   - Beneficial topologies are sparse; one topology rarely dominates all tasks.
   - Refs: `2502.02533...:55, :116`

5. **Majority voting without deliberative critique**
   - Underperforms critique+refinement patterns in cited comparisons.
   - Refs: `2502.04506...:46, :58, :79`

6. **Single-dimension context-window scaling**
   - Shows bounded returns; better to allocate compute across context+batch+turn.
   - Refs: `2511.15738...:42, :44, :54`

7. **Debate-heavy workflows on low-depth tasks**
   - Overhead may outweigh marginal gains when depth is low/width-dominated.
   - Refs: `2510.04311...:47, :105`

8. **Long-horizon context accumulation without drift controls**
   - Can induce belief/behavior drift in agent behavior.
   - Refs: `2511.01805...:45, :75, :108, :123`

### Decision heuristic (method selection)
- Prefer **SAS-first** for routine/low-depth tasks.
- Escalate to **conditional MAS debate** on detected disagreement, high-depth reasoning, or high-stakes checks.
- Enforce **round caps + consensus stop + overhead budget**.
- Avoid fixed topology lock-in; periodically re-search/topology-test.
- Add drift monitoring for long sessions.
