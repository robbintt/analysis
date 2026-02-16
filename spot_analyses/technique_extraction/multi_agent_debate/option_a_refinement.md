# Multi-Agent Debate — Option A (Semantic Refinement)

**Date:** 2026-02-15  
**Input:** 153 core_contribution summaries (`/tmp/multi_agent_debate_core_contributions.txt`)  
**Goal:** Reconcile grep buckets into mechanism-level debate families for answer-quality improvement.

---

## Refined Taxonomy (Semantic)

### 1) Debate Orchestration Protocols (~42)
Design of the interaction process itself: turn schedule, challenge/rebuttal structure, and stopping flow.

**Sub-families**
- Fixed multi-round vs adaptive-round debate
- Reflection/backtracking-enhanced trajectories
- Structured debate templates (claim-counterclaim-justification)

**Representative papers:** 2409.14051, 2507.03928, 2510.16645, 2511.11306, 2602.00454

---

### 2) Role & Persona-Structured Deliberation (~50)
Explicit role decomposition and persona diversity to widen reasoning coverage and avoid mode collapse.

**Sub-families**
- Author/reviewer/meta-reviewer patterns
- Solver/reflector or prosecutor/defense/judge triads
- Persona-induced perspective diversity

**Representative papers:** 2505.11811, 2509.11656, 2512.02405, 2601.21936, 2512.07132

---

### 3) Critic/Judge/Verifier-Mediated Debate (~35)
Quality control via dedicated critic/judge agents or verifier-like scoring components.

**Sub-families**
- Agent-as-judge evaluators
- Checklist-driven or rubric-driven critics
- Error-detection and claim-verification mediators

**Representative papers:** 2502.08514, 2507.19090, 2508.02584, 2511.01014, 2511.06396

---

### 4) Consensus & Decision Fusion (~24)
Mechanisms for converting multiple debated trajectories into one final answer.

**Sub-families**
- Majority/weighted voting
- Confidence-weighted consensus
- Adjudicator and reconciliation strategies

**Representative papers:** 2509.14034, 2509.23537, 2502.08514, 2504.02128, 2512.22625

---

### 5) Disagreement/Confidence Regulation (~18)
Methods that use disagreement signals, confidence, or anti-sycophancy controls to steer debate.

**Sub-families**
- Silent-agreement and sycophancy mitigation
- Confidence expression and calibration-aware routing
- Conflict-triggered additional deliberation

**Representative papers:** 2505.21503, 2509.23055, 2510.06843, 2508.13743, 2601.12091

---

### 6) Adaptive Efficiency & Budgeted Debate (~22)
Reducing MAD overhead while preserving gains.

**Sub-families**
- Selective trigger/gating of debate
- Token/latency-aware sparse debate
- Compression/streaming for lower inference cost

**Representative papers:** 2511.11306, 2510.05059, 2602.00454, 2507.08664, 2509.20502

---

### 7) Evidence-Grounded Debate (Retrieval/Tools) (~24)
Grounding debate turns in retrieved evidence or tool outputs.

**Sub-families**
- Debate-augmented RAG
- Evidence cross-verification loops
- Tool-recruited debate for multimodal reasoning

**Representative papers:** 2505.18581, 2507.09174, 2512.07132, 2508.02584, 2509.17395

---

### 8) Learning from Debate Traces (~22)
Using debate interactions as supervision signals for post-training.

**Sub-families**
- Debate trace distillation
- Debate-based RL / preference optimization
- Self-improvement via synthetic debates

**Representative papers:** 2506.03541, 2509.15172, 2601.22297, 2511.05528, 2506.02689

---

## Overlay Layers (not core technique roots)

### A) Safety/Alignment/Security Uses (~20)
Debate deployed for jailbreak defense, risk analysis, and trustworthy evaluation.

### B) Domain Instantiations & Benchmarks (~40+)
Medical, legal, scientific, and multimodal application settings plus dedicated benchmarks.

---

## Semantic Reconciliation Notes

### What Option C got right
- High-recall identification of the core MAD design axes (protocol, roles, consensus, critics).
- Correct signal that efficiency/cost control is now a first-order concern.
- Correctly captured debate-to-training pipelines as a growing subfield.

### What Option C over-split
- Benchmark/evaluation and domain buckets are contextual overlays, not primary mechanisms.
- Confidence/disagreement effects were partially fragmented across consensus and safety buckets.

### What Option C under-expressed
- The centrality of **disagreement regulation** (anti-sycophancy, silent-agreement mitigation).
- The distinction between **debate runtime mechanisms** and **debate-derived training methods**.

### Edge/tangential papers
- A small tail are broad MAS theory, context papers, or sparse summaries with weak mechanism detail.
