# Multi-Agent Debate — Option C (Grep-Seeded)

**Date:** 2026-02-15  
**Group:** `multi_agent_debate` (153 papers)  
**Coverage:** 147/153 matched (96.1%)  
**Unmatched:** 6 papers (mostly broad MAS context/theory or malformed/empty summary).

---

## Group Definition Used (Phase 0)

Primary phrase anchors over 2025 corpus:

- `multi-agent debate`
- `llm debate`
- `multi-agent deliberation`
- `debate framework`
- `debate-driven`
- `debate-based`

Scope-tightening filter:
- Excluded obvious context-only title classes (`survey`, `review`, `position`, `benchmark`, `technical report`, `literature review`) before insertion.
- Deduplicated by `arxiv_id` via `spot_analysis_paper_groups` uniqueness.

Result: 154 candidate files -> 153 unique papers.

---

## Grep-Seeded Categories

### 1) Core MAD Frameworks (48 papers)
Patterns: `multi-agent debate`, `MAD`, `multi-LLM debate`, `debate framework`, `debating systems`, `debate-driven`, `argumentative exchanges`.

Canonical debate-framework papers that treat debate itself as the main mechanism.

### 2) Debate Protocol Design (46 papers)
Patterns: `multi-turn`, `multi-round`, `iterative`, `structured debate`, `deliberation protocol`, `reflection`, `backtracking`.

How debate proceeds over time: rounds, challenge/response, reflection cycles, and trajectory edits.

### 3) Role/Persona Team Design (63 papers)
Patterns: `persona`, `role-based`, `specialized agents`, `author/reviewer/meta-reviewer`, `moderator`, `solver/reflector`.

Agent-role assignment and persona diversity as mechanism for improved reasoning coverage.

### 4) Aggregation & Consensus (23 papers)
Patterns: `consensus`, `voting`, `majority`, `unanimous`, `adjudicate`, `convergence`.

Mechanisms for combining competing agent outputs into final answers.

### 5) Critic/Judge/Verifier Mediation (32 papers)
Patterns: `critic`, `judge`, `reviewer`, `verification`, `error detection`, `claim verification`, `oversight`.

Third-party critique/evaluation agents that shape debate quality.

### 6) Confidence/Disagreement-Aware Control (16 papers)
Patterns: `confidence`, `uncertainty`, `disagreement`, `sycophancy`, `silent agreement`, `overconfident`, `bias mitigation`.

Debate control based on conflict signals and calibration/anti-sycophancy dynamics.

### 7) Efficiency & Scaling Controls (24 papers)
Patterns: `efficient`, `cost`, `latency`, `token`, `sparse`, `gating`, `adaptive trigger`, `memory compression`, `TTFT`.

Cost-aware MAD methods that reduce unnecessary rounds/tokens.

### 8) Retrieval/Tool/Evidence-Augmented Debate (25 papers)
Patterns: `RAG`, `retrieval`, `evidence`, `tool`, `knowledge graph`, `cross-verification`.

Debate grounded by retrieved evidence/tools to reduce hallucination and improve factuality.

### 9) Training from Debate Traces (25 papers)
Patterns: `distill`, `post-training`, `reinforcement learning`, `self-improvement`, `preference optimization`.

Using debate interactions as supervision signals for model improvement.

### 10) Safety/Security/Alignment Debate Uses (20 papers)
Patterns: `safety`, `alignment`, `jailbreak`, `harmful`, `deceptive`, `security`, `trustworthy`, `guard`.

Debate mechanisms applied to guardrail construction, risk identification, and safer decision support.

### 11) Benchmark & Evaluation Infrastructure (40 papers)
Patterns: `benchmark`, `evaluation`, `dataset`, `metrics`, `study`.

Debate-focused evaluation suites and comparative studies (high overlap with all mechanism categories).

### 12) Domain Overlays (29 papers)
Patterns: `medical`, `legal`, `scientific`, `finance`, `education`, `table reasoning`, `code generation`, `robot`.

Application overlays where MAD is instantiated in domain-specific pipelines.

---

## Overlap Notes

- Strong overlap among **Core MAD**, **Protocol Design**, **Role/Persona**, and **Critic/Judge**.
- **Benchmark/Evaluation** and **Domain Overlays** are support/context buckets, not pure mechanism roots.
- **Efficiency** and **Confidence/Disagreement** are cross-cutting controls that often operate jointly.

---

## Coverage Summary

- Total papers: **153**
- Matched by grep categories: **147 (96.1%)**
- Unmatched: **6** (mostly broad MAS context papers or weakly debate-specific summaries)
