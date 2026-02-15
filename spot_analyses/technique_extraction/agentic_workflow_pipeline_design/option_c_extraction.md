# Agentic Workflows / Pipeline Design — Grep-Seeded Extraction (Option C)

- **Group:** `agentic_workflow_pipeline_design`
- **Total papers:** 92
- **Matched to >=1 category:** 91
- **Coverage:** 98.9%
- **Unmatched:** 1 paper (niche autonomous ML experimentation pipeline phrasing)

## Categories

### 1) Multi-Agent Collaboration Patterns (37)
Workflows using multiple specialized agents (often role-based) to jointly solve tasks via collaboration/debate/discussion loops.

Pattern: `multi.agent|collaborat\w*|debate|discussion|consensus|agent.team`

### 2) Orchestration / Control Layer (33)
Explicit orchestration logic: orchestrator/meta-agent, routing, scheduling, coordination, or control-plane mechanisms.

Pattern: `orchestrat\w*|orchestrator|meta.agent|agent.routing|\brouting\b|router|scheduler|coordinat\w*|control.plane`

### 3) Workflow Synthesis / Design / Optimization (32)
Methods that generate, design, optimize, or compile workflows (often automatically or adaptively).

Pattern: `workflow.generation|workflow.design|automatic.workflow|workflow.synth\w*|template|compiler|meta.learn\w*|bayesian|evolution\w*|optimi\w*|agentic.workflow`

### 4) Hierarchical & Modular Decomposition (27)
Architectures that decompose tasks into subtasks with hierarchical or modular agent structure.

Pattern: `hierarchical|modular|decompos\w*|task.allocat\w*|role.specific|speciali\w*.agent|actor.factory|multi.stage|subtask`

### 5) Efficiency & Serving Optimization (24)
Latency/cost/token optimization for agentic workflows, including serving and scheduling concerns.

Pattern: `latency|cost|token|serving|scheduling|throughput|efficien\w*|speculative|optimi\w*`

### 6) Planner-Executor Architectures (16)
Explicit planner-executor (or plan-and-execute) decomposition and related planner-centric control.

Pattern: `planner|executor|plan.and.execute|planner.executor|meta.planner|director.agent`

### 7) Evaluation & Benchmarking of Workflows (14)
Benchmarks, evaluations, audits, and comparative studies for workflow/agent architecture quality.

Pattern: `benchmark|evaluation|survey|review|audit|comparator|case.study`

### 8) Tool / Retrieval-Orchestrated Pipelines (13)
Agentic workflows that explicitly coordinate external tools, MCP/tool-calling, retrieval, or RAG modules.

Pattern: `tool.call\w*|tool.use|mcp|model.context.protocol|retrieval|\brag\b|langgraph|graph.executable|api`

### 9) Memory & Context Management (12)
Workflow designs focused on long-horizon context handling, episodic memory, state management, and overflow mitigation.

Pattern: `memory|episodic.memory|context.window|long.horizon|state.management|cache|overflow|summarization`

### 10) Safety / Guardrails / Red-Teaming in Workflows (10)
Architectures that embed safety checks, guardrails, or red-teaming into multi-agent workflows.

Pattern: `safety|guardrail|red.team\w*|verification|robust\w*|defen\w*|risk`

---

## Coverage Notes

- Category overlap is high and expected (e.g., planner-executor papers are often also hierarchical + orchestration-control + efficiency).
- The unmatched paper (`2506.05542`) is still in-scope conceptually (autonomous agentic ML pipeline), but wording did not hit current category patterns.
- The group includes a minority of benchmark/survey and domain-specific application papers; these are still useful because many describe concrete workflow mechanisms.
