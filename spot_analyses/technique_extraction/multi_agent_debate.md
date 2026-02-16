# Multi-Agent Debate — Final Analysis

**Date:** 2026-02-15  
**Group:** `multi_agent_debate` (153 papers, 2025 corpus)  
**Grep Coverage:** 147/153 (96.1%)  
**Sources:** [Option C (grep-seeded)](multi_agent_debate/option_c_extraction.md) · [Option A (semantic refinement)](multi_agent_debate/option_a_refinement.md)

---

## Method Summary

- **Option C:** high-recall grep pass over debate/deliberation summaries to surface recurring mechanism buckets.
- **Option A:** semantic consolidation into mechanism-level families and explicit separation of overlays (domains/benchmarks/safety applications).
- **Merge rule:** preserve Option C recall; adopt Option A category boundaries where overlap is heavy.

---

## Final Taxonomy: 8 Core Technique Categories + 2 Overlay Categories

Categories **1–8** are mechanism-level debate techniques. Categories **9–10** are overlays (application/evaluation context).

### 1) Debate Orchestration Protocols (~42)
How agents interact over turns/rounds and how debate trajectories are edited.

- Multi-round/iterative challenge-rebuttal protocols
- Reflection/backtracking trajectory updates
- Structured turn templates

**Key papers:** 2409.14051, 2507.03928, 2510.16645, 2511.11306, 2602.00454  
**Agreement:** Strong Option C + Option A agreement.

### 2) Role & Persona-Structured Deliberation (~50)
Deliberation quality improved through role decomposition and perspective diversity.

- Author/reviewer/meta-reviewer patterns
- Solver/reflector or prosecutor/defense/judge patterns
- Persona-induced diverse reasoning

**Key papers:** 2505.11811, 2509.11656, 2512.02405, 2601.21936, 2512.07132  
**Agreement:** High confidence in both extractions.

### 3) Critic/Judge/Verifier-Mediated Debate (~35)
Dedicated critic/judge/verifier agents score and constrain the debate process.

- Agent-as-judge evaluators
- Checklist/rubric critics
- Claim/error verification loops

**Key papers:** 2502.08514, 2507.19090, 2508.02584, 2511.01014, 2511.06396  
**Agreement:** Stable core family.

### 4) Consensus & Decision Fusion (~24)
Mechanisms that combine multiple debated outputs into a final answer.

- Majority/weighted voting
- Confidence-weighted reconciliation
- Adjudication and convergence control

**Key papers:** 2509.14034, 2509.23537, 2502.08514, 2504.02128, 2512.22625  
**Agreement:** Strong with moderate overlap to categories 3 and 5.

### 5) Disagreement/Confidence Regulation (~18)
Use disagreement and confidence signals to avoid collapse/sycophancy and trigger better debate.

- Silent-agreement and sycophancy mitigation
- Confidence-aware debate continuation
- Conflict-sensitive control

**Key papers:** 2505.21503, 2509.23055, 2510.06843, 2508.13743, 2601.12091  
**Agreement:** Option A sharpened this as a distinct mechanism family.

### 6) Adaptive Efficiency & Budgeted Debate (~22)
Reduce debate cost while preserving quality improvements.

- Selective debate triggering
- Token/latency-aware sparse debate
- Compression/streaming optimizations

**Key papers:** 2511.11306, 2510.05059, 2602.00454, 2507.08664, 2509.20502  
**Agreement:** Present in both; Option A merged several efficiency fragments.

### 7) Evidence-Grounded Debate (Retrieval/Tools) (~24)
Grounding debate steps in retrieved evidence and tools.

- Debate-augmented RAG
- Evidence cross-verification
- Tool-recruited multi-agent reasoning

**Key papers:** 2505.18581, 2507.09174, 2512.07132, 2508.02584, 2509.17395  
**Agreement:** High confidence.

### 8) Learning from Debate Traces (~22)
Debate interactions become supervision for post-training.

- Debate-trace distillation
- Debate-based RL / preference optimization
- Self-improvement pipelines

**Key papers:** 2506.03541, 2509.15172, 2601.22297, 2511.05528, 2506.02689  
**Agreement:** Clear growth area across both passes.

### 9) Overlay: Safety/Security/Alignment Applications (~20)
Debate used for jailbreak defense, risk analysis, and trustworthy system evaluation.

**Key papers:** 2511.06396, 2511.21460, 2512.00349, 2512.02282, 2601.11903

### 10) Overlay: Domain + Benchmark Infrastructure (~40+)
Domain-specific deployments (medical/legal/science/etc.) and evaluation suites.

**Key papers:** 2502.08916, 2509.17395, 2511.08317, 2510.25110, 2512.09935

---

## Extraction Reconciliation

### Where Option C and Option A agree
- Protocol design, role diversity, and critic/judge mediation are the backbone of MAD methods.
- Consensus mechanisms and evidence grounding are recurring and robustly represented.
- Efficiency-aware debate control is now a first-order concern.

### What Option A added
- Clear separation between **runtime debate mechanisms** and **debate-derived training methods**.
- Elevated **disagreement/confidence regulation** as a standalone technique family.
- Clear distinction between mechanism categories and overlay/context categories.

### Merge / drop decisions
- Merged: several efficiency sub-buckets into **Adaptive Efficiency & Budgeted Debate**.
- Merged: confidence/disagreement signals previously scattered across consensus/safety into one mechanism family.
- Demoted: benchmark-heavy and domain-heavy clusters to overlay status.

---

## Coverage Reconciliation

| Metric | Count |
|---|---:|
| Total papers in group | 153 |
| Grep-matched (Option C) | 147 (96.1%) |
| Semantically classifiable into core technique categories | ~132 |
| Overlay/context-heavy (domain + benchmark dominant) | ~15 |
| Clearly tangential to debate mechanisms | ~5 |
| Empty/malformed entries | ~1 |

---

## Application / Domain Summary (overlay)

| Domain | ~Papers | Note |
|---|---:|---|
| Multimodal/Vision reasoning | ~23 | Debate used for VQA, multimodal fact-checking, and evidence adjudication |
| Medical/clinical decision support | ~11 | Safety- and reliability-sensitive debate workflows |
| Scientific/research workflows | ~14 | Hypothesis generation, reviewer-style debates, idea evaluation |
| Legal/governance simulation | ~9 | Courtroom-style and deliberative role structures |
| Misinformation/claim verification | ~6 | Debate + retrieval/evidence fusion for factual robustness |

---

## Paper List

See [papers.md](multi_agent_debate/papers.md) (153 papers).

## Extraction Artifacts

- [overview.md](multi_agent_debate/overview.md)
- [option_c_extraction.md](multi_agent_debate/option_c_extraction.md)
- [option_a_refinement.md](multi_agent_debate/option_a_refinement.md)
