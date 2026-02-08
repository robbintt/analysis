# LLM-as-Judge Applications: A Comprehensive Guide for Heterogeneous Agentic Workflows

Date: 2026-02-08
Grounded in: 2,000+ research analysis documents across `research_analysis_v1/` and `research_analysis_v2/`, plus `lm_council_methodology/` synthesis artifacts.

---

## Abstract

This document provides a comprehensive, research-grounded guide for building and deploying LLM-based judges across heterogeneous agentic workflows. Drawing from over 2,000 analyzed research papers spanning reward modeling, RLHF, multi-agent systems, safety evaluation, and test-time compute scaling, it presents actionable architectures, domain-specific application patterns, failure modes, and operational guidance for organizations and individual contributors building judge systems at scale.

The core finding: **LLM judges are most effective when they are domain-specialized, reasoning-transparent, calibrated against human judgment, and integrated with process-level (not just outcome-level) evaluation**. Universal judge architectures underperform selective, task-routed designs—mirroring the selective council finding from the LM Council methodology.

---

## Table of Contents

1. [Foundations: What Is an LLM Judge?](#1-foundations-what-is-an-llm-judge)
2. [Judge Architectures](#2-judge-architectures)
3. [Training Paradigms for Judge Models](#3-training-paradigms-for-judge-models)
4. [Application Domains](#4-application-domains)
5. [Integrating Judges into Agentic Workflows](#5-integrating-judges-into-agentic-workflows)
6. [Multi-Agent Judge Systems](#6-multi-agent-judge-systems)
7. [Calibration, Bias, and Failure Modes](#7-calibration-bias-and-failure-modes)
8. [Safety and Guardrail Judges](#8-safety-and-guardrail-judges)
9. [Test-Time Compute Scaling with Judges](#9-test-time-compute-scaling-with-judges)
10. [Operational Deployment Guide](#10-operational-deployment-guide)
11. [Reference Architecture](#11-reference-architecture)
12. [Research Grounding Index](#12-research-grounding-index)

---

## 1. Foundations: What Is an LLM Judge?

### 1.1 Definition

An LLM judge is a language model—or an ensemble thereof—used to evaluate, score, rank, verify, or filter outputs produced by other models, agents, or systems. Judges replace or augment human evaluation in scenarios where manual annotation does not scale.

### 1.2 Judge vs. Reward Model vs. Verifier

| Component | Input | Output | Training Signal | Use Phase |
|-----------|-------|--------|-----------------|-----------|
| **Judge** | Prompt + response(s) | Score, ranking, critique, or pass/fail | Varies (RLHF, rubric, constitutional) | Evaluation, filtering, routing |
| **Reward Model** | Prompt + response | Scalar reward | Human preference pairs (Bradley-Terry) | Policy optimization (PPO, DPO) |
| **Process Reward Model (PRM)** | Partial trajectory | Per-step reward | Step-level annotations or MCTS rollouts | Inference-time search, beam selection |
| **Verifier** | Candidate answer | Binary correct/incorrect | Ground-truth labels or formal specs | Best-of-N selection, test-time scaling |

**Key insight from corpus**: These components exist on a spectrum. The Reward Reasoning Model (RRM) demonstrates that adding chain-of-thought reasoning to reward models yields 14.1 percentage point improvements on GPQA, blurring the line between reward models and generative judges. ToolRM shows that domain-specific reward models (for tool calling) outperform general-purpose LLM-as-judge approaches by 25% on functional correctness.

### 1.3 Why LLM Judges Matter Now

Three converging trends from the research corpus make LLM judges critical infrastructure:

1. **Agentic workflow proliferation**: Multi-step, tool-using agents require evaluation at every decision point—tool selection, plan validity, intermediate reasoning, and final output. Human evaluation cannot scale to the volume of decisions made by autonomous agents.

2. **Test-time compute scaling**: Research on scaling test-time compute (ATTS framework) shows that verification-guided search at inference time can double agent success rates (10% → 20% on WebArena with 32x compute). Judges are the enabling mechanism.

3. **RLHF evolution**: The field is moving from binary preference pairs toward multi-dimensional, process-aware, reasoning-transparent evaluation—requiring judges that can articulate *why* one output is better, not just *which* is better.

---

## 2. Judge Architectures

### 2.1 Architecture Taxonomy

Based on patterns extracted across the corpus, judge architectures fall into six families:

#### 2.1.1 Pointwise Scoring
- **Description**: Judge evaluates a single response against a rubric or criteria, producing a scalar score or structured assessment.
- **Strengths**: Simple, parallelizable, no comparison artifacts.
- **Weaknesses**: Calibration drift, scale sensitivity.
- **Use when**: Filtering, threshold-based gating, quality monitoring.

#### 2.1.2 Pairwise Comparison
- **Description**: Judge compares two responses and selects the better one, optionally with justification.
- **Strengths**: Relative judgments are cognitively easier and more reliable than absolute scoring.
- **Weaknesses**: Position bias (first-option preference), O(n²) comparisons for ranking.
- **Use when**: Preference data collection, RLHF training pairs, A/B evaluation.
- **Corpus evidence**: Bradley-Terry pairwise preference modeling is foundational to ToolRM and standard reward model training.

#### 2.1.3 Listwise Ranking
- **Description**: Judge ranks N candidates simultaneously.
- **Strengths**: More efficient than pairwise for large candidate sets; captures relative quality across the full set.
- **Weaknesses**: Context length limitations, order effects.
- **Use when**: Best-of-N selection, test-time compute scaling.
- **Corpus evidence**: ATTS framework finds listwise verification outperforms voting and scoring for agentic tasks.

#### 2.1.4 Generative Critique
- **Description**: Judge produces natural language feedback identifying specific strengths, weaknesses, and suggestions.
- **Strengths**: Interpretable, actionable, supports iterative refinement.
- **Weaknesses**: Harder to aggregate, may be verbose.
- **Use when**: Reflection loops, human-in-the-loop review, self-correction agents.
- **Corpus evidence**: Think-J demonstrates that learning explicit reasoning traces before judgment yields 84.9% accuracy, surpassing classifier-based approaches.

#### 2.1.5 Aspect-Based Verification
- **Description**: Multiple specialized sub-judges each evaluate one dimension (correctness, style, safety, relevance), then aggregate.
- **Strengths**: Modular, composable, enables targeted improvements.
- **Weaknesses**: Aggregation design is non-trivial; aspect correlations can be missed.
- **Use when**: Multi-dimensional quality assessment, heterogeneous evaluation criteria.
- **Corpus evidence**: Multi-Agent Verification (MAV) shows 48.7% accuracy on MATH using aspect verifiers, vs. 37.2% for self-consistency.

#### 2.1.6 Process Reward Models
- **Description**: Judge evaluates each step of a multi-step reasoning chain, assigning per-step rewards.
- **Strengths**: Dense feedback signal, enables search-guided inference, identifies where reasoning fails.
- **Weaknesses**: Requires step-level supervision or rollout-based approximation.
- **Use when**: Mathematical reasoning, multi-step agents, planning tasks.
- **Corpus evidence**: MASPRM achieves +30.7 EM points on GSM8K by applying process rewards to multi-agent transcripts.

### 2.2 Architecture Selection Matrix

| Workflow Type | Recommended Architecture | Rationale |
|---------------|--------------------------|-----------|
| Single-turn QA | Pointwise scoring | Fast, sufficient for simple evaluation |
| Preference collection for RLHF | Pairwise comparison | Aligns with Bradley-Terry training |
| Best-of-N agent selection | Listwise ranking | Efficient at scale per ATTS findings |
| Self-correction loops | Generative critique | Actionable feedback for iterative refinement |
| Multi-criteria evaluation | Aspect-based verification | Modular assessment of heterogeneous quality dimensions |
| Math/code reasoning chains | Process reward model | Step-level feedback catches intermediate errors |
| Tool-calling agents | Domain-specific reward model | ToolRM shows 25% improvement over general judges |
| Safety filtering | Constitutional + pointwise | Principle-adherence scoring (C3AI framework) |

---

## 3. Training Paradigms for Judge Models

### 3.1 Paradigm Overview

The corpus reveals five primary training paradigms for building judge models, each with distinct trade-offs:

### 3.2 Supervised Fine-Tuning on Human Judgments

- **Method**: Train on datasets of human evaluations (scores, preferences, critiques).
- **Strengths**: Direct signal from ground truth; simple training pipeline.
- **Limitations**: Expensive to collect; annotator disagreement introduces noise; does not scale.
- **Corpus evidence**: Efficient Online RFT shows that training on just 10K human-justified preference pairs (HH-Rationales) yields 96.2% accuracy on RewardBench.
- **Best for**: High-stakes domains where human judgment is definitive and budget permits annotation.

### 3.3 RLHF / RLAIF for Judge Optimization

- **Method**: Use reinforcement learning to optimize judge behavior against preference signals (human or AI-generated).
- **Key variants**:
  - **RLHF**: Human preferences as reward signal.
  - **RLAIF**: AI-generated preferences as reward signal (Curriculum-RLAIF).
  - **DPO**: Direct optimization on preference pairs without explicit reward model.
  - **GRPO**: Group Relative Policy Optimization with rule-based rewards.
- **Corpus evidence**: The GRO framework unifies all RL-based and RL-free methods under neural structured bandit prediction—the key differentiator is **baseline choice and advantage calculation**, not the algorithm family. Rule-based rewards outperform process reward models for reasoning tasks.
- **Critical finding**: Curriculum-RLAIF demonstrates that **training difficulty progression matters**—starting with easy (contrastive) pairs and progressing to hard (random) pairs yields superior generalization. Training on all data simultaneously fails on difficult samples due to label noise correlation with difficulty.

### 3.4 Self-Evolved / Annotation-Free Training

- **Method**: Generate training signal from the model's own outputs using verification or rollout-based supervision.
- **Corpus evidence**: Reward Reasoning Model (RRM) uses GRPO with rule-based rewards to train reasoning-capable reward models without explicit reasoning trace annotations—achieving 14.1pp improvement on GPQA. MASPRM uses MCTS rollout supervision to train process reward models without step-level human annotations.
- **Best for**: Domains where ground-truth verification is possible (math, code, tool execution) but step-level annotation is prohibitive.

### 3.5 Plug-and-Play Adaptation

- **Method**: Augment a frozen instruction-tuned model with lightweight adapters (LoRA) for judge capability.
- **Corpus evidence**: Efficient Online RFT achieves 96.2% RewardBench accuracy with only 0.8% parameter overhead (rank-16 LoRA on 7B base), preserving the base model's generalist capabilities.
- **Best for**: Organizations needing to rapidly deploy judges without full fine-tuning infrastructure; multi-domain judge deployment where the same base model serves different judge roles.

### 3.6 Pessimistic Reward Modeling

- **Method**: Train reward models with minimax optimization to be deliberately conservative, preventing reward hacking.
- **Corpus evidence**: PET (Pessimistic rEward Tuning) achieves 55.6% win rate on TL;DR without KL constraints, maintaining stability at KL divergence 12–15 vs. 10 for standard methods. Shifts robustness responsibility from the policy to the reward model architecture.
- **Best for**: High-stakes production deployments where reward hacking is a critical risk; scenarios where KL-constrained optimization is infeasible.

### 3.7 Training Paradigm Selection Guide

| Scenario | Recommended Paradigm | Key Consideration |
|----------|----------------------|-------------------|
| Abundant human annotations | Supervised fine-tuning | Quality of annotator agreement |
| Scaling beyond human annotation | RLAIF with curriculum | Easy-to-hard progression critical |
| Verifiable domains (math, code) | Self-evolved / GRPO | Ground-truth verification enables annotation-free training |
| Rapid deployment, limited compute | Plug-and-play LoRA | 0.8% parameter overhead, preserves base capabilities |
| Production safety-critical | Pessimistic reward modeling | Prevents reward hacking without KL constraints |
| Multi-domain judge fleet | LoRA adapters on shared base | Different judge adapters for different domains |

---

## 4. Application Domains

### 4.1 Code Evaluation Judges

**Research grounding**: "Don't Judge Code by Its Cover" (2505.16222), SWE-Bench-CL, Guided Code Generation framework.

**Application patterns**:
- **Functional correctness**: Judge whether generated code produces correct outputs for given inputs.
- **Code quality**: Evaluate style, maintainability, security, and performance characteristics.
- **Bug detection**: Identify logical errors, edge case failures, and vulnerability patterns.

**Critical failure mode**: LLM judges exhibit systematic biases in code evaluation—authority comments, self-declared correctness, illusory complexity (dummy functions), and variable naming all influence judgments independently of functional correctness. Judgment reversals (Incorrect → Correct) occur due to authority bias. Test case generation does not mitigate these biases.

**Recommended approach**:
- Use **execution-based verification** (test execution, fuzzing) as the primary judge for functional correctness—LLM judges alone are unreliable.
- Reserve LLM judges for **qualitative assessment** (readability, documentation quality, architectural patterns) where execution-based metrics are unavailable.
- Implement **functional isolation**: evaluate code logic separately from code presentation to mitigate surface-level biases.
- For code review workflows, pair LLM judges with static analysis tools and test coverage metrics.

### 4.2 Mathematical Reasoning Verification

**Research grounding**: MASPRM, Reward Reasoning Model, Process-Supervised RL, VisTIRA.

**Application patterns**:
- **Step-level verification**: Process reward models evaluate each reasoning step, enabling identification of where errors occur.
- **Answer verification**: Outcome reward models check final answers against ground truth.
- **Proof validation**: Judges assess logical validity of multi-step mathematical proofs.

**Recommended approach**:
- Deploy **process reward models** for dense feedback on multi-step reasoning chains (+30.7 EM points on GSM8K via MASPRM).
- Use **MCTS rollout supervision** for annotation-free PRM training—propagate final correctness backward to estimate per-step rewards.
- Combine PRMs with **beam search** or **best-of-N selection** at inference time for optimal test-time compute scaling.
- For novel mathematical domains, leverage **self-evolved training** (RRM approach) that generates reasoning traces without manual annotation.

### 4.3 Tool Use and Function Calling Judges

**Research grounding**: ToolRM, ToolScope, Tool-to-Agent Retrieval, Verifiably Safe Tool Use.

**Application patterns**:
- **Tool selection correctness**: Judge whether the agent selected the appropriate tool for the subtask.
- **Parameter validity**: Evaluate whether function arguments are correctly specified.
- **Execution safety**: Verify that tool invocations will not cause harmful side effects.

**Critical finding**: General-purpose LLM judges significantly underperform domain-specific tool reward models. ToolRM demonstrates 25% improvement over baselines using a Bradley-Terry model trained on tool-specific preference data. Most common errors are Incorrect Parameter Value (650 instances) and Incorrect Function Name (403 instances) in FC-RewardBench.

**Recommended approach**:
- Build **domain-specific tool reward models** rather than relying on general-purpose LLM judges.
- Train on **tool-specific preference data** with reward-centering regularization.
- Implement **pre-execution verification** judges that assess tool calls before execution, not just post-hoc.
- For safety-critical tool use, employ **formal verification** where possible, with LLM judges as a complementary soft check.

### 4.4 Factuality and Hallucination Detection

**Research grounding**: GroundSight, Causal Fact-Checking, Pix2Fact, RAG evaluation frameworks.

**Application patterns**:
- **Grounded generation verification**: Judge whether outputs are supported by provided context/sources.
- **Claim-level decomposition**: Break responses into individual claims and verify each independently.
- **Attribution checking**: Verify that cited sources actually support the claims made.

**Recommended approach**:
- Use **grounded visual reasoning** with confidence-based filtering (GroundSight achieves 51.91% hallucination reduction).
- Deploy **causal reasoning judges** rather than simple entailment checks—causal structure provides more robust factuality assessment.
- Implement **claim decomposition** pipelines: split response → extract claims → verify each claim → aggregate.
- For RAG systems, judge both **retrieval relevance** and **generation faithfulness** as separate dimensions.

### 4.5 Safety and Toxicity Evaluation

**Research grounding**: AgentDoG, 3D-Guard Layer, SafeFlow, Constitutional AI (C3AI), Control-Theoretic Guardrails.

**Application patterns**:
- **Content safety**: Evaluate outputs for harmful, toxic, or inappropriate content.
- **Behavioral safety**: Assess whether agent actions comply with safety constraints.
- **Adversarial robustness**: Test whether judges maintain accuracy under adversarial inputs.

See [Section 8](#8-safety-and-guardrail-judges) for detailed treatment.

### 4.6 Instruction Following Assessment

**Research grounding**: Mixture-of-Clustered-Experts, StructEval, instruction tuning literature.

**Application patterns**:
- **Constraint adherence**: Judge whether output follows all specified constraints (format, length, style, content restrictions).
- **Task completion**: Evaluate whether the response fully addresses the instruction.
- **Format compliance**: Verify structured output formats (JSON, XML, tables, specific templates).

**Recommended approach**:
- Use **constraint decomposition**: parse instructions into individual constraints, evaluate each independently, aggregate.
- For structured outputs, combine **schema validation** (deterministic) with **semantic correctness judges** (LLM-based).
- Deploy **hierarchical evaluation**: first check hard constraints (format, length), then assess soft quality dimensions (helpfulness, depth).

### 4.7 Creative and Open-Ended Generation

**Research grounding**: Generative AI and Creativity survey, summarization quality studies, BigGen Bench.

**Application patterns**:
- **Subjective quality**: Evaluate writing style, creativity, engagement, and coherence.
- **Preference alignment**: Score outputs against target audience preferences.
- **Diversity assessment**: Judge whether generated content is novel vs. derivative.

**Critical challenge**: Open-ended evaluation is where LLM judges are most susceptible to biases (length bias, style mimicry, sycophancy). Bridging Human and LLM Judgments research shows systematic deviations that require explicit calibration.

**Recommended approach**:
- Always **calibrate against human judgments** using post-hoc alignment (logit trick yields +8% accuracy improvement).
- Use **multi-judge panels** with diverse model families to reduce systematic bias.
- Define **explicit rubrics** with concrete anchor examples for each quality level.
- Deploy **preference-strength-aware models** (ResponseRank approach) that distinguish weak vs. strong preferences rather than treating all preferences as equal magnitude.

### 4.8 Multi-Turn Conversation Evaluation

**Research grounding**: Training Dialogue Systems by AI Feedback, DH-RAG, multi-turn benchmarks.

**Application patterns**:
- **Turn-level quality**: Evaluate individual turns for relevance, helpfulness, and coherence.
- **Conversation-level coherence**: Judge whether the full dialogue maintains consistency, avoids contradictions, and progresses logically.
- **Context maintenance**: Assess whether the agent properly tracks and utilizes conversation history.

**Recommended approach**:
- Evaluate at **both turn and conversation levels**—turn-level judges miss conversation-level degradation patterns.
- Use **sliding window evaluation** for long conversations to manage context limits.
- Track **context drift metrics**: measure how well the agent maintains topic coherence and factual consistency across turns.
- For conversation training, use **AI feedback on overall dialogue impression** rather than individual turn scoring.

### 4.9 Retrieval-Augmented Generation (RAG) Quality

**Research grounding**: RAG survey, Dense Passage Retrieval, FastV-RAG, retrieval quality benchmarks.

**Application patterns**:
- **Retrieval relevance**: Judge whether retrieved passages are relevant to the query.
- **Generation faithfulness**: Evaluate whether the generated response is faithful to retrieved content.
- **Integration quality**: Assess how well retrieved information is synthesized into a coherent response.

**Recommended approach**:
- Decompose RAG evaluation into **three independent judge dimensions**: retrieval precision, generation faithfulness, and response completeness.
- Use **citation verification judges** that check each cited source against the claim it supports.
- Deploy **contrastive evaluation**: judge with and without retrieval to measure the contribution of retrieved context.

---

## 5. Integrating Judges into Agentic Workflows

### 5.1 Judge Integration Points

Across the eight agentic workflow categories identified in the corpus, judges integrate at distinct points:

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENTIC WORKFLOW                              │
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │  PLAN    │───▶│  SELECT  │───▶│ EXECUTE  │───▶│ RESPOND  │  │
│  │          │    │  TOOL    │    │  ACTION  │    │          │  │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘  │
│       │               │               │               │        │
│  ┌────▼─────┐    ┌────▼─────┐    ┌────▼─────┐    ┌────▼─────┐  │
│  │  PLAN    │    │  TOOL    │    │ PROCESS  │    │ OUTCOME  │  │
│  │  JUDGE   │    │  JUDGE   │    │  JUDGE   │    │  JUDGE   │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              SAFETY JUDGE (continuous)                    │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │          REFLECTION JUDGE (triggered on failure)          │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Workflow-Specific Judge Patterns

#### 5.2.1 Orchestration Workflows
**Pattern**: Route evaluation decisions to appropriate specialist judges based on task type.
**Judge role**: Score orchestration decisions—did the system select the right sub-agent, the right tool, the right decomposition?
**Corpus evidence**: LM Council methodology demonstrates that SAS-first routing with MAS escalation outperforms static multi-agent deployment. Judges enable this routing by evaluating task complexity and disagreement signals.

#### 5.2.2 Multi-Agent Collaboration
**Pattern**: Multiple agents collaborate on a task; judges assess collaboration quality.
**Judge role**: Evaluate whether multi-agent outputs are coherent, non-redundant, and complete. Score individual agent contributions and interaction quality.
**Corpus evidence**: MASPRM provides per-agent progress evaluation in partial inter-agent transcripts, enabling targeted feedback on which agents contribute value.

#### 5.2.3 Autonomous Agent Operations
**Pattern**: Agents operate with minimal human oversight; judges provide ongoing quality assurance.
**Judge role**: Validate decision-making quality, safety constraint adherence, and task completion without human intervention.
**Corpus evidence**: AgentDoG's three-dimensional taxonomy (Risk Source → Failure Mode → Consequence) provides a structured framework for autonomous agent evaluation. SafeFlow adds transactional safety guarantees.

#### 5.2.4 Tool-Using Agent Workflows
**Pattern**: Agents select and invoke external tools; judges verify tool use correctness.
**Judge role**: Score tool selection appropriateness, parameter correctness, and result interpretation.
**Corpus evidence**: ToolRM demonstrates that specialized tool reward models outperform general-purpose judges by 25%. Pre-execution verification prevents costly errors.

#### 5.2.5 Planning Agent Workflows
**Pattern**: Agents decompose goals into plans; judges evaluate plan quality.
**Judge role**: Assess plan validity, temporal ordering, goal coverage, and feasibility.
**Corpus evidence**: Surveys on LLM-based agent evaluation show that advanced LLMs significantly lag behind symbolic planners on long-horizon tasks—judges can identify planning failures before execution.

#### 5.2.6 Reflection and Self-Correction Loops
**Pattern**: Agents reflect on their outputs and self-correct; judges guide the reflection.
**Judge role**: Assess whether reflection trajectories identify actual errors and propose valid corrections.
**Corpus evidence**: ATTS framework shows threshold-based reflection outperforms continuous reflection. Judges should trigger reflection only when confidence is below a threshold, not on every output.

#### 5.2.7 Chain-of-Thought Reasoning
**Pattern**: Agents generate explicit reasoning chains; judges verify reasoning validity.
**Judge role**: Verify logical coherence, factual accuracy, and completeness of reasoning steps.
**Corpus evidence**: Process reward models (PRMs) evaluate per-step reasoning quality. Chain-of-thought monitorability research identifies this as a key safety opportunity—but one that is fragile and can be subverted.

#### 5.2.8 Test-Time Compute Scaling
**Pattern**: Generate multiple candidate solutions at inference time; judges select the best.
**Judge role**: Score and rank candidates to identify optimal outputs given a compute budget.
**Corpus evidence**: See [Section 9](#9-test-time-compute-scaling-with-judges).

### 5.3 Judge Placement Decision Framework

| Decision Factor | Place Judge Before Action | Place Judge After Action |
|-----------------|--------------------------|--------------------------|
| Action is reversible | ✗ | ✓ |
| Action has side effects | ✓ | ✗ |
| Low latency requirement | ✗ (skip or async) | ✓ |
| High-stakes outcome | ✓ | ✓ (both) |
| Training signal needed | ✗ | ✓ |
| Safety-critical | ✓ (always) | ✓ (always) |

---

## 6. Multi-Agent Judge Systems

### 6.1 When to Use Multi-Agent Judges

Applying the LM Council methodology's selective council finding to judge design:

**Use multi-agent judges when**:
- Single-judge confidence is low or ambiguous
- The evaluation requires multiple distinct competencies (safety + quality + factuality)
- Disagreement between judges is informative (debate-worthy)
- Stakes are high enough to justify additional compute cost

**Default to single-agent judges when**:
- Evaluation criteria are well-defined and narrow
- Latency constraints are tight
- The domain has a reliable specialist judge
- Cost/quality ROI of multi-judge is not justified

### 6.2 Multi-Agent Judge Architectures

#### 6.2.1 Panel of Judges
- **Structure**: N independent judges evaluate the same output; results are aggregated.
- **Aggregation**: Majority vote, weighted average, or consensus with threshold.
- **Corpus evidence**: MAV shows that deploying 64 verifiers on 4 candidates outperforms 4 verifiers on 64 candidates—**verifier density matters more than candidate diversity**.

#### 6.2.2 Debate-Based Evaluation
- **Structure**: Multiple judges argue for and against an output, then a meta-judge decides.
- **Corpus evidence**: LM Council methodology finds that **disagreement-triggered debate outperforms always-on debate** in cost/quality balance. Use debate only when initial judge panel shows significant disagreement.

#### 6.2.3 Hierarchical Judges
- **Structure**: Fast/cheap judges filter obvious cases; expensive judges handle ambiguous ones.
- **Corpus evidence**: Mirrors the SAS-first → MAS escalation pattern. Default to efficient single-judge evaluation; escalate to multi-judge only when complexity warrants it.

#### 6.2.4 Weak-to-Strong Verification
- **Structure**: Multiple weak judges approximate a strong judge's evaluation.
- **Corpus evidence**: MAV demonstrates that **9 weak verifiers can approximate a strong supervisor**—enabling scalable oversight without access to stronger models.

### 6.3 Multi-Agent Judge Operational Rules

Adapted from LM Council decision rules:

1. **Default to single judge** (mirrors SAS-first default).
2. **Escalate to multi-judge** when: disagreement threshold exceeded, confidence below minimum, task classified as high-stakes.
3. **Cap debate rounds** at 3 with consensus stop (mirrors debate protocol guardrails).
4. **Monitor coordination overhead**: multi-judge systems should not exceed 200–300% of single-judge cost without proportional quality improvement.
5. **Use dynamic routing**: assign different judge models/configurations per query type, not a fixed global panel.
6. **Instrument for context drift**: long multi-judge deliberations can introduce context drift—monitor and bound.

---

## 7. Calibration, Bias, and Failure Modes

### 7.1 Known Biases in LLM Judges

Based on systematic evidence from the corpus:

| Bias Type | Description | Severity | Mitigation |
|-----------|-------------|----------|------------|
| **Position bias** | Preference for first/last option in pairwise or listwise evaluation | High | Randomize presentation order; average across orderings |
| **Length bias** | Preference for longer responses regardless of quality | High | Length-controlled evaluation; penalize unnecessary verbosity |
| **Style mimicry** | Preference for outputs that match the judge model's own style | Medium | Use diverse judge model families; cross-family evaluation |
| **Authority bias** | Influenced by authoritative framing in outputs | High (code) | Functional isolation; separate logic from presentation |
| **Sycophancy** | Agreement with user's stated preference in the prompt | Medium | Blind evaluation; remove user opinion from judge prompt |
| **Illusory complexity** | Higher scores for superficially complex outputs (dummy functions, unnecessary abstractions) | High (code) | Complexity-independent evaluation criteria |
| **Recency bias** | Overweighting recent context in multi-turn evaluation | Medium | Full-context evaluation; sliding window with anchoring |

### 7.2 Calibration Against Human Judgment

**Research grounding**: "Bridging Human and LLM Judgments" (2508.12792).

**Key findings**:
- LLM judges exhibit **systematic deviations** from human judgment that are modelable and correctable.
- Raw LLM assessments show **poor calibration**—the confidence expressed in judge outputs does not reliably correspond to actual correctness probability.
- Post-hoc alignment using ordinal logistic regression and the "logit trick" algorithm yields **+8% accuracy improvement** (69% → 77% for GPT-4) with only ~200 human-labeled calibration samples.

**Recommended calibration procedure**:
1. Collect a calibration set of ~200 human judgments on representative examples.
2. Model LLM judge outputs as **biased linear transformations** of latent human preference scores.
3. Use covariates (output length, complexity, domain) to characterize specific biases.
4. Apply post-hoc logistic regression to align judge scores with human distributions.
5. Re-calibrate periodically as model and data distributions shift.

### 7.3 Preference Strength

**Research grounding**: ResponseRank / Responsive Reward Modeling.

**Critical insight**: Standard preference learning treats all preferences equally, but preferences vary in strength. A marginal preference ("A is slightly better than B") should be weighted differently than a strong preference ("A is clearly superior to B").

**Recommended approach**:
- Learn **cardinal utility differences**, not just ordinal rankings.
- Use **stratified local comparison**: partition data into comparable strata to control systemic variation.
- Extract preference strength from **relative differences** in proxy signals (inter-annotator agreement, response time), not absolute values.
- Evaluate judges using **Pearson Distance Correlation (PDC)**, which assesses cardinal utility prediction separately from ordinal accuracy.

### 7.4 Critical Failure Modes

#### 7.4.1 Reward Hacking
- **Description**: Optimized models learn to exploit imperfections in the judge/reward model rather than genuinely improving quality.
- **Mitigation**: Pessimistic reward modeling (PET); ensemble judges; periodic red-teaming of judge models.

#### 7.4.2 Distribution Shift
- **Description**: Judge accuracy degrades when evaluating outputs from models or domains not represented in training data.
- **Mitigation**: Curriculum training (easy → hard); periodic recalibration; domain-specific judges for specialized workflows.

#### 7.4.3 Judge-Model Collusion
- **Description**: When judge and generator share the same base model, the judge may preferentially score outputs that match its own distribution.
- **Mitigation**: Use cross-family evaluation (different model families for judge and generator); diverse judge panels.

#### 7.4.4 Context Window Saturation
- **Description**: Judge performance degrades when the evaluation context (prompt + response + rubric + examples) exceeds effective context utilization.
- **Mitigation**: Prioritize rubric and examples; use summarization for long contexts; test judge accuracy as a function of context length.

---

## 8. Safety and Guardrail Judges

### 8.1 Safety Judge Taxonomy

Based on AgentDoG's three-dimensional framework:

```
SAFETY EVALUATION = Risk Source × Failure Mode × Consequence

Risk Source (WHERE):  User input | Agent decision | Tool execution | Environment
Failure Mode (HOW):  Misuse | Misalignment | Capability failure | Context loss
Consequence (WHAT):  Harm to user | Data breach | System compromise | Reputation
```

**Key finding**: Risk source identification is the hardest dimension (32.4% accuracy vs. 59.2% for failure mode classification)—implying that safety judges should invest disproportionate effort in source attribution.

### 8.2 Multi-Layer Safety Architecture

Based on the corpus synthesis, effective safety judging requires multiple layers:

**Layer 1: Input Screening**
- Pre-process user inputs for known attack patterns (prompt injection, jailbreaking).
- Fast, rule-based + lightweight classifier hybrid.

**Layer 2: Action Verification**
- Pre-execution judge for agent actions, especially tool calls with side effects.
- Verify actions against safety constraints before execution.
- **Corpus evidence**: SafeFlow's principled protocol requires transactional safety guarantees—actions are verified before commitment.

**Layer 3: Output Evaluation**
- Post-generation content safety assessment.
- Constitutional principle adherence (C3AI framework).
- **Corpus evidence**: C3AI identifies that humans prefer positive framing, but models adhere better to negative principles ("Don't do X" > "Do Y")—design constitutions accordingly.

**Layer 4: Continuous Monitoring**
- Ongoing behavioral monitoring across conversation turns.
- Context drift detection for multi-turn interactions.
- **Critical insight from corpus**: Refusal alone is insufficient—harm arises from evolving interactions and downstream cascades, not single tokens. Control-theoretic approaches that proactively correct trajectories outperform passive blocking.

### 8.3 Safety Judge Design Principles

1. **Hierarchical scoring over binary classification**: Use AgentDoG's three-dimensional taxonomy instead of simple safe/unsafe labels.
2. **Proactive correction over passive refusal**: Control-theoretic guardrails that steer toward safe trajectories outperform stop-and-refuse approaches.
3. **Never "set-and-forget"**: Safety judges require persistent monitoring, periodic recalibration, and adversarial testing.
4. **Context-aware + context-independent dual evaluation**: Deploy both a context-aware judge (tracks conversation state) and a context-independent content moderation judge (consistent baseline) per the education safety research.
5. **Source attribution investment**: Allocate disproportionate judge capacity to identifying *where* safety risks originate, as this is the hardest subtask.

---

## 9. Test-Time Compute Scaling with Judges

### 9.1 Framework

**Research grounding**: ATTS (Agent Test-Time Scaling), Multi-Agent Verification, Scaling Test-Time Compute for LLM Agents.

Test-time compute scaling uses judges to improve agent performance at inference time by generating multiple candidates and selecting the best. The ATTS framework identifies four components:

1. **Parallel Sampling**: Generate N candidate outputs/trajectories.
2. **Sequential Revision**: Iteratively refine candidates based on judge feedback.
3. **Verification/Merging**: Score candidates using judges; select or merge the best.
4. **Rollout Diversity**: Maximize diversity of generated candidates (temperature sampling, prompt variation).

### 9.2 Key Findings

- **32x compute budget** can double agent success rates (10% → 20% on WebArena).
- **Listwise verification** outperforms voting and scoring for agentic tasks.
- **Threshold-based reflection** (judge triggers revision only below confidence threshold) outperforms continuous reflection in efficiency.
- **Verifier density > candidate diversity**: 64 verifiers on 4 candidates outperform 4 verifiers on 64 candidates (MAV finding).
- **Weak-to-strong**: 9 weak verifiers approximate 1 strong supervisor.

### 9.3 Practical Scaling Guide

| Compute Budget | Strategy | Judge Configuration |
|----------------|----------|---------------------|
| 1x (baseline) | Single pass | No judge (or fast classifier gate) |
| 2–4x | Best-of-N | Single judge, pointwise scoring |
| 4–16x | Best-of-N + revision | Judge scores + critique → revision → re-score |
| 16–64x | Parallel sampling + multi-verifier | Multiple verifiers, listwise ranking |
| 64x+ | Full MCTS / beam search | Process reward model guiding search |

### 9.4 Diminishing Returns and Cost Management

- Standard parallel sampling shows **diminishing returns** beyond ~16 candidates.
- To maximize ROI: invest in **verifier quality/diversity** rather than candidate quantity.
- Use **3D budgeting** (context + batch + turn) from LM Council methodology to bound total compute.
- Track judge latency on the critical path—judges should not become the bottleneck.

---

## 10. Operational Deployment Guide

### 10.1 Deployment Checklist

Adapted from the LM Council methodology's 4-phase rollout framework:

#### Phase 1: Shadow Deployment
- [ ] Deploy judge alongside existing evaluation (human or rule-based).
- [ ] Compare judge outputs to ground truth without acting on judge decisions.
- [ ] Measure agreement rate, calibration, latency, and cost.
- [ ] Identify systematic biases via covariate analysis.

#### Phase 2: Guarded Deployment
- [ ] Use judge for low-stakes decisions (logging, monitoring, suggestions).
- [ ] Human override available for all judge decisions.
- [ ] A/B test judge-guided vs. baseline workflows.
- [ ] Calibrate confidence thresholds based on shadow deployment data.

#### Phase 3: Progressive Deployment
- [ ] Expand judge authority to medium-stakes decisions.
- [ ] Implement escalation rules: judge handles routine cases, humans handle edge cases.
- [ ] Monitor for distribution shift and recalibrate periodically.
- [ ] Instrument cost/quality/latency tracking dashboards.

#### Phase 4: Full Deployment
- [ ] Judge operates autonomously for all targeted decisions.
- [ ] Continuous monitoring with drift detection.
- [ ] Periodic adversarial testing (red-teaming the judge).
- [ ] Regular recalibration against fresh human judgment samples.

### 10.2 Monitoring and Observability

**Essential metrics for production judge systems**:

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| Agreement rate | Judge vs. human agreement on calibration set | < 80% triggers recalibration |
| Confidence calibration | Correlation between stated confidence and actual accuracy | Brier score > 0.25 |
| Latency P99 | 99th percentile judge evaluation time | Domain-specific; should not exceed 2x median |
| Cost per evaluation | Total compute cost per judge invocation | Budget-dependent; track trend |
| Bias drift | Change in bias metrics over time | Statistical significance test |
| Adversarial robustness | Judge accuracy under adversarial inputs | < 70% triggers review |
| Context utilization | Effective use of provided context window | Degradation with length signals saturation |

### 10.3 Cost Optimization Strategies

1. **Tiered judging**: Use fast/cheap judges for easy cases; escalate to expensive judges only for ambiguous cases (mirrors SAS → MAS escalation).
2. **Caching**: Cache judge decisions for identical or near-identical evaluation contexts.
3. **Batching**: Batch multiple evaluations into single judge calls where architecture permits.
4. **LoRA adapters**: Use lightweight adapters on shared base models instead of separate fine-tuned models per domain (0.8% parameter overhead per Efficient Online RFT).
5. **Distillation**: Distill expensive judge models into smaller, faster models for routine evaluations.

---

## 11. Reference Architecture

### 11.1 Selective Judge Router Architecture

Mirroring the LM Council methodology's Selective Council Stack v1:

```
┌──────────────────────────────────────────────────────────────┐
│                    JUDGE ROUTER                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ Input: (task_type, complexity, stakes, domain)          │ │
│  │ Output: judge_config (architecture, model, parameters)  │ │
│  └─────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │  POINTWISE │  │  PAIRWISE  │  │  LISTWISE  │            │
│  │  SCORER    │  │  COMPARER  │  │  RANKER    │            │
│  └────────────┘  └────────────┘  └────────────┘            │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │ GENERATIVE │  │  ASPECT    │  │  PROCESS   │            │
│  │  CRITIC    │  │  VERIFIER  │  │  REWARD    │            │
│  └────────────┘  └────────────┘  └────────────┘            │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                   GOVERNANCE LAYER                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ COMPUTE  │  │ LATENCY  │  │  SAFETY  │  │  DRIFT   │   │
│  │ GOVERNOR │  │ GOVERNOR │  │ GOVERNOR │  │ MONITOR  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
├──────────────────────────────────────────────────────────────┤
│                 CALIBRATION LAYER                             │
│  ┌──────────────────┐  ┌──────────────────┐                 │
│  │  HUMAN ALIGNMENT │  │  BIAS CORRECTION │                 │
│  │  (logit trick)   │  │  (covariates)    │                 │
│  └──────────────────┘  └──────────────────┘                 │
└──────────────────────────────────────────────────────────────┘
```

### 11.2 Module Descriptions

| Module | Function | Config Dimensions |
|--------|----------|-------------------|
| **Judge Router** | Selects judge architecture and model based on task characteristics | `task_type`, `complexity_score`, `stakes_level`, `domain`, `latency_budget` |
| **Pointwise Scorer** | Single-response evaluation against rubric | `rubric`, `scale`, `criteria_weights` |
| **Pairwise Comparer** | Two-response preference judgment | `position_randomization`, `tie_allowed` |
| **Listwise Ranker** | N-response simultaneous ranking | `max_candidates`, `ranking_depth` |
| **Generative Critic** | Natural language feedback generation | `critique_depth`, `suggestion_required` |
| **Aspect Verifier** | Dimension-specific binary verification | `aspects[]`, `aggregation_method` |
| **Process Reward** | Per-step trajectory evaluation | `step_granularity`, `rollback_threshold` |
| **Compute Governor** | Bounds total judge compute budget | `max_tokens`, `max_calls`, `cost_ceiling` |
| **Latency Governor** | Ensures judge latency stays within budget | `p99_target`, `timeout`, `fallback_judge` |
| **Safety Governor** | Enforces safety constraints on judge behavior | `constitution`, `escalation_rules` |
| **Drift Monitor** | Detects distribution shift in judge inputs/outputs | `window_size`, `drift_threshold`, `alert_channel` |
| **Human Alignment** | Post-hoc calibration against human judgments | `calibration_set_size`, `regression_model` |
| **Bias Correction** | Covariate-based bias adjustment | `bias_covariates[]`, `correction_method` |

### 11.3 Integration Patterns for 1000+ Heterogeneous Workflows

For organizations deploying judges across many diverse workflows:

**Pattern 1: Shared Judge Infrastructure**
- Deploy a common judge router and governance layer.
- Each workflow registers its evaluation criteria and domain.
- Router selects from a shared pool of judge models/adapters.
- Governance layer enforces organization-wide cost, latency, and safety constraints.

**Pattern 2: Domain-Specialized Judge Pools**
- Group workflows by domain (code, safety, reasoning, creative, tool use).
- Train domain-specific judge models or LoRA adapters per pool.
- Route evaluations to the appropriate domain pool.
- Cross-domain evaluations use multi-judge panels from relevant pools.

**Pattern 3: Hierarchical Judge Cascade**
- Tier 1: Fast, cheap universal judges handle 80% of routine evaluations.
- Tier 2: Domain-specific judges handle 15% of domain-specialized evaluations.
- Tier 3: Multi-judge panels with human escalation handle 5% of high-stakes/ambiguous cases.

---

## 12. Research Grounding Index

### 12.1 Primary Research Papers

This document synthesizes findings from the following key papers analyzed in the corpus:

| Topic | Key Paper | Finding |
|-------|-----------|---------|
| Reasoning judges | Think-J (Learning to Think for LLM-as-a-Judge) | 84.9% accuracy via learned reasoning traces |
| Plug-and-play judges | Efficient Online RFT with LLM Judges | 96.2% RewardBench accuracy, 0.8% parameter overhead |
| Reward reasoning | Reward Reasoning Model (RRM) | +14.1pp on GPQA via chain-of-thought reward modeling |
| Multi-agent process rewards | MASPRM | +30.7 EM points on GSM8K with annotation-free training |
| Agent reasoning rewards | Exploring Reasoning Reward Model for Agents | Unified feedback strategy outperforms text-only or reward-only |
| Tool evaluation | ToolRM | 25% improvement via domain-specific tool reward models |
| Code judge bias | Don't Judge Code by Its Cover | 6 systematic bias categories; test generation does not mitigate |
| Human-LLM calibration | Bridging Human and LLM Judgments | +8% accuracy via logit trick with ~200 calibration samples |
| Constitutional AI | C3AI | Models adhere better to negative principles than positive framing |
| Multi-agent verification | MAV | 9 weak verifiers ≈ 1 strong supervisor; verifier density > candidate diversity |
| Test-time scaling | ATTS / Scaling Test-Time Compute for Agents | 32x compute → 2x success rate; listwise verification optimal |
| Safety diagnostics | AgentDoG | Risk source identification hardest (32.4% accuracy) |
| Safe agent protocol | SafeFlow | Transactional safety guarantees for autonomous agents |
| Control-theoretic safety | From Refusal to Recovery | Proactive correction outperforms passive blocking |
| Preference strength | ResponseRank | Cardinal utility differences > ordinal rankings |
| Pessimistic rewards | PET (Pessimistic rEward Tuning) | 55.6% win rate without KL constraints |
| Curriculum training | Curriculum-RLAIF | Easy-to-hard progression critical; simultaneous training fails |
| RLHF unification | GRO (One Framework to Rule Them All) | All RLHF methods differ only in baseline and advantage calculation |
| Agent evaluation survey | Survey on Evaluation of LLM-Based Agents | LLMs lag symbolic planners on long-horizon tasks |
| Agent safety | 3D-Guard Layer | Integrated agentic AI safety for edge deployment |

### 12.2 Supporting Methodology

This document also builds on the `lm_council_methodology/` synthesis, which provides:
- Selective council strategy (SAS-first, conditional MAS escalation)
- Decision rules checklist (50+ gating rules across 10 rule families)
- Do/Don't methodology matrix (resolved contradictions across 10 methodology families)
- 4-phase rollout framework (shadow → guarded → progressive → full)
- Reference architecture (7-module Selective Council Stack v1)
- 3D budgeting model (context + batch + turn)
- Governance layer design (compute, latency, safety governors)

### 12.3 Corpus Statistics

- **Total research papers analyzed**: 2,000+
- **Papers directly relevant to LLM-as-judge**: 50+
- **Domain coverage**: code evaluation, mathematical reasoning, tool use, factuality, safety, instruction following, creative generation, multi-turn conversation, RAG, calibration, constitutional AI, scalable oversight
- **Temporal coverage**: 2025–2026 frontier research

---

## Appendix A: Quick-Start Decision Tree

```
START: You need to evaluate an agent output
│
├─ Is the output verifiable by execution? (code, math, tool call)
│   ├─ YES → Use execution-based verification + domain-specific reward model
│   └─ NO → Continue below
│
├─ Is this a single-turn or multi-turn evaluation?
│   ├─ SINGLE-TURN → Pointwise scoring or pairwise comparison
│   └─ MULTI-TURN → Conversation-level judge + turn-level judges
│
├─ Is this safety-critical?
│   ├─ YES → Multi-layer safety architecture (Section 8)
│   │         + Constitutional principles (negative framing)
│   │         + Continuous monitoring
│   └─ NO → Continue below
│
├─ Do you need to select from N candidates?
│   ├─ N ≤ 4 → Best-of-N with pointwise scoring
│   ├─ 4 < N ≤ 64 → Listwise ranking (ATTS finding)
│   └─ N > 64 → Process reward model + beam search
│
├─ Is the evaluation multi-dimensional?
│   ├─ YES → Aspect-based verification with aggregation
│   └─ NO → Single-criterion judge
│
├─ Is judge confidence sufficient?
│   ├─ YES → Accept judgment
│   └─ NO → Escalate to multi-judge panel (Section 6)
│           Use disagreement-triggered debate
│           Cap at 3 rounds with consensus stop
│
└─ DONE: Apply calibration (Section 7.2) and monitor for drift
```

## Appendix B: Anti-Patterns

Derived from failure-first analysis across the corpus:

| Anti-Pattern | Why It Fails | Evidence |
|-------------|--------------|----------|
| **Universal judge for all domains** | Domain-specific judges outperform generalists by 25%+ | ToolRM, code bias findings |
| **Always-on multi-judge panels** | Coordination overhead exceeds quality gains for routine evaluations | LM Council: 200–300% overhead band |
| **Treating all preferences equally** | Ignores preference magnitude; weak and strong preferences weighted the same | ResponseRank: cardinal > ordinal |
| **Training on all data simultaneously** | Fails on difficult samples due to label noise | Curriculum-RLAIF: easy-to-hard critical |
| **Refusal-only safety** | Harm comes from interaction trajectories, not single outputs | Control-theoretic guardrails |
| **Fixed judge configuration** | Different tasks require different judge architectures and models | Dynamic routing evidence |
| **Judge without calibration** | Systematic 8%+ accuracy gap vs. calibrated judges | Bridging Human and LLM Judgments |
| **Continuous reflection** | Less efficient than threshold-triggered reflection | ATTS findings |
| **Ignoring context drift** | Judge accuracy degrades in long multi-turn evaluations | LM Council drift monitoring |
| **Same model family for judge and generator** | Style mimicry and distribution collusion | Cross-family evaluation evidence |

## Appendix C: Glossary

| Term | Definition |
|------|------------|
| **LLM Judge** | A language model used to evaluate, score, rank, verify, or filter outputs from other models or agents |
| **Reward Model (RM)** | A neural network trained to predict human preferences, producing scalar rewards for policy optimization |
| **Process Reward Model (PRM)** | A reward model that evaluates individual steps in a multi-step reasoning chain |
| **Outcome Reward Model (ORM)** | A reward model that evaluates only the final output, not intermediate steps |
| **RLHF** | Reinforcement Learning from Human Feedback—training paradigm using human preferences to align model behavior |
| **RLAIF** | Reinforcement Learning from AI Feedback—using AI-generated preferences instead of human annotations |
| **DPO** | Direct Preference Optimization—offline preference optimization without explicit reward model training |
| **GRPO** | Group Relative Policy Optimization—RL method using rule-based rewards and group-relative advantages |
| **Bradley-Terry Model** | Statistical model for pairwise comparisons; foundational to reward model training |
| **Best-of-N (BoN)** | Generate N candidates and select the highest-scoring one via a judge or reward model |
| **Constitutional AI** | Training methodology using a set of principles (constitution) to guide model behavior |
| **Test-Time Compute Scaling** | Allocating additional compute at inference time (not training time) to improve output quality |
| **Aspect Verifier** | A specialized judge that evaluates one specific dimension of quality (e.g., correctness, safety, style) |
| **Calibration** | Adjusting judge outputs so stated confidence corresponds to actual accuracy |
| **Reward Hacking** | When an optimized model exploits imperfections in the judge/reward model rather than genuinely improving |
| **Context Drift** | Degradation in evaluation quality as conversation length increases and context accumulates |
| **SAS** | Single-Agent System—one model handling a task without multi-agent coordination |
| **MAS** | Multi-Agent System—multiple models collaborating on a task with coordination overhead |

---

*This document is a living reference. As the research corpus grows, update findings, add new application domains, and recalibrate recommendations against emerging evidence.*
