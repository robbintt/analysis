# Agentic Workflows / Pipeline Design — LLM Refinement Pass (Option A)

Source: `option_c_extraction.md` + semantic review of representative `core_contribution` samples.

## Main Refinement

Option C is high-coverage but slightly flat. The strongest structure is a **3-layer workflow stack**:

1. **Control Layer**: orchestration policy (routing/scheduling/meta-agents)
2. **Structure Layer**: planner-executor and hierarchical role decomposition
3. **Execution Layer**: tool/retrieval integration + memory/context handling + efficiency mechanisms

Safety/evaluation are cross-cutting constraints over all three layers.

---

## Recommended Merges / Splits

### Merge A: `collaboration` + `planner_executor` + `hierarchical_modular`
These are highly overlapping descriptions of workflow structure.

**Merged category:** **Workflow Topology Design**
- Planner-executor decomposition
- Hierarchical role trees
- Specialized-role collaboration
- Constrained topology and traversal strategies

Why: Most papers counted in collaboration are actually about topology choices (who does what, in what order), not collaboration as an isolated technique.

### Keep B: `orchestration_control` as separate
This is the runtime policy layer (routing/scheduling/orchestrator/meta-agent) and is conceptually distinct from static topology.

### Keep C: `workflow_synthesis` as separate
This is meta-level design automation (automatic workflow generation, optimization, Bayesian/evolutionary search, meta-agent workflow design).

### Split D: `efficiency_serving`
Current category mixes two different ideas:
- **Systems-level efficiency** (latency/cost/throughput/serving)
- **Algorithmic efficiency** (fewer LLM calls via compilation/meta-tools/speculative tool calls)

### Keep E: `memory_context` + `tool_retrieval`
Both are core execution mechanics and can stay separate.

### Reframe F: `evaluation`
Treat as **infrastructure category** (benchmarking/auditing), not core workflow design technique.

---

## Refined Taxonomy (Final)

### 1) Orchestration Policy & Control
Runtime decision-making over agent/tool invocation:
- dynamic routing
- orchestrator agents
- schedulers/coordinators
- control-plane abstractions

### 2) Workflow Topology Design
How workflow graph is structured:
- planner-executor
- hierarchical decomposition
- role-specialized multi-agent collaboration
- staged/stepwise traversal

### 3) Workflow Synthesis & Self-Optimization
Methods that generate or improve workflows automatically:
- automatic workflow generation
- meta-agent design loops
- evolutionary/Bayesian/meta-learning optimization
- template/compile-style synthesis

### 4) Context & Memory Management
Long-horizon reliability mechanisms:
- context overflow mitigation
- episodic/procedural memory
- plan-aware compression/summarization
- state persistence across turns

### 5) Tool/Retrieval-Oriented Execution
External capability integration at workflow level:
- tool-calling orchestration
- MCP / API mediation
- retrieval/RAG module composition
- graph-executable tool pipelines

### 6) Efficiency & Serving for Agentic Workflows
Compute/latency/cost controls:
- serving-aware scheduling
- token/call budget control
- speculative tool calling
- workflow compilation into reusable meta-tools

### 7) Safety, Guardrails, and Governance
Safety-as-workflow mechanisms:
- multi-agent red teaming pipelines
- policy/guardrail insertion points
- verification/defense modules embedded in workflow

### 8) Evaluation & Benchmarking Infrastructure (supporting)
- benchmark suites for workflow robustness/quality
- auditable/explainable workflow artifacts
- evaluation loops for iterative improvement

---

## Techniques Option C Underweights

1. **Workflow compilation/compression** (compile repeated traces into reusable tools or condensed plans)
2. **Single-agent simulation of multi-agent workflows** (replacing explicit multi-agent execution while preserving workflow behavior)
3. **Human-in-the-loop orchestration oversight** (visualization/inspection/editing of workflow state)
4. **Serving-runtime co-design** (workflow design + serving scheduler jointly optimized)

---

## Domain Clusters (not core categories)

Notable application clusters inside the group:
- biomedical/clinical pipelines
- scientific workflow automation
- text-to-SQL / data workflows
- software engineering workflows

These should be treated as application slices over the refined taxonomy, not taxonomy roots.
