# Test-Time Compute Scaling

## Corpus Coverage

- **987 papers** in 2025 corpus (52K total) — union of "test-time scaling/compute" and "inference-time scaling/compute"
- 15 papers in 2024 corpus (28K files)
- 82 papers use both terms interchangeably

## Scope

Techniques for allocating additional compute at inference to improve output quality — reasoning budgets, search strategies, verification, and self-consistency methods.

---

## Technique Taxonomy

Extraction used grep-seeded category discovery ([option_c_extraction.md](test_time_compute_scaling/option_c_extraction.md)) followed by semantic refinement ([option_a_refinement.md](test_time_compute_scaling/option_a_refinement.md)). Coverage: 76.4% of papers matched to ≥1 category. The remaining ~24% are benchmarks, evaluations, or tangential mentions.

### Three-Layer Architecture

Most test-time compute scaling systems combine techniques from three layers:

1. **Compute Allocation** — how much compute to spend and where
2. **Search & Generation** — how to produce candidate outputs
3. **Evaluation & Selection** — how to judge and pick the best output

### Tier 1: Core Test-Time Scaling Techniques

#### Chain-of-Thought & Reasoning Traces (~100 papers)

Explicit verbalized reasoning at inference time. The foundational technique that most other TTC methods build on.

**Sub-categories:**
- CoT prompting variants (zero-shot, few-shot, difficulty-aware, compressed)
- CoT training (SFT on traces, critical token fine-tuning)
- Reasoning token mechanisms (thinking tokens, continue-thinking tokens, pause tokens)
- Domain transfer (CoT for vision, audio, time series, tables)
- CoT efficiency (trace compression, critical token identification)

**Key finding:** CoT is increasingly treated as a controllable resource — models trained to adjust reasoning depth based on problem complexity, rather than applying uniform reasoning to all inputs.

#### Tree/Graph Search (~45 papers)

Structured search over reasoning paths using explicit tree or graph exploration.

**Sub-categories:**
- MCTS-based reasoning (~15 papers) — Monte Carlo Tree Search for proof search, planning, trajectory construction
- Beam search variants (~10 papers) — entropy-gated branching, selective beam search
- Tree-of-Thought frameworks (~8 papers) — including ToTRL for training tree reasoning via RL
- Dynamic branching (~5 papers) — branch at uncertainty, prune low-value paths
- Graph/DAG reasoning (~5 papers) — non-tree structured reasoning

**Key finding:** Entropy-gated branching (branch only at high-uncertainty steps) consistently outperforms uniform beam search while using less compute.

#### Best-of-N & Parallel Sampling (~50 papers)

Generate multiple candidates in parallel, select the best via voting, scoring, or consensus.

**Sub-categories:**
- Best-of-N with reward model scoring
- Majority voting / self-consistency
- Multi-model routing (ROBON — route across models, not just samples)
- Adaptive-N (vary sample count by difficulty)

**Key finding:** Standard BoN is provably suboptimal (multiple papers demonstrate this). Adaptive-N and sequential routing achieve better performance-cost tradeoffs.

#### Iterative Self-Refinement (~55 papers)

Sequential improvement of outputs through reflection, correction, and revision.

**Sub-categories:**
- Self-refinement (generate → critique → revise loops)
- Self-correction (detect and fix errors in own output)
- Reflection-based methods (explicit introspection before revision)
- Multi-turn sequential reasoning

**Key finding:** Self-refinement without external feedback has limited gains. The most effective methods combine self-refinement with verification signals (verifier-guided refinement).

#### Process Reward Models (~32 papers)

Step-level reward signals that evaluate intermediate reasoning steps.

**Key finding:** PRMs are the critical enabler for tree search and sequential refinement — they provide the signal that guides exploration. Papers that improve PRM training (e.g., training from MCTS rollouts, multi-agent PRM) directly improve downstream TTC scaling.

#### Learned Verifiers (~65 papers)

Trained models for output verification and selection — parametric verifiers, LLM-as-judge, formal/symbolic verification.

**Sub-categories:**
- Parametric verifiers (trained verification models)
- LLM-as-judge (using LLMs to evaluate outputs)
- Self-verification (model checking its own outputs)
- Formal/symbolic verification (~10 papers) — code execution, proof checking
- Generative verifiers (verifiers that produce reasoning about correctness)

**Key finding:** Generative verifiers (those that explain *why* an output is correct/incorrect) outperform discriminative verifiers (binary correct/incorrect). Dynamic verifiers that combine fast and slow verification (e.g., Dyve) offer the best efficiency-accuracy tradeoffs.

#### Adaptive Compute Allocation (~50 papers)

Dynamic compute budgeting based on task difficulty, model confidence, or performance feedback.

**Sub-categories:**
- Overthinking mitigation (~20 papers) — early stopping, length control, detecting redundant reasoning
- Query-adaptive allocation (~12 papers) — bandit-based allocation, utility optimization, difficulty routing
- Scaling law characterization (~10 papers) — empirical compute-performance curves
- Fast/slow routing (~8 papers) — model cascading, routing between inference modes

**Key finding:** Overthinking is a major practical problem. Multiple papers show that reasoning models waste 30-60% of tokens on easy problems. The most promising solutions use confidence/entropy-based early stopping.

### Tier 2: Enabling Techniques

| Category | Papers | Role |
|---|---|---|
| **RL Training for Reasoning** | ~80 | Trains models to reason better via GRPO, PPO, DPO, RLHF. Enables all Tier 1 techniques by improving base reasoning quality. Note: ~20 papers are about RL-style *search* at inference, not training. |
| **Thinking Modes & Architecture** | ~20 | Dual-mode models (System 1/2), thinking budgets, mode switching. Architectural foundation for adaptive compute. |
| **Reasoning Distillation** | ~45 | Compresses expensive TTC into smaller/faster models. The efficiency counterpart to scaling up. |
| **Inference Efficiency** | ~40 | Speculative decoding, KV cache optimization, pruning. Makes each TTC step cheaper. |
| **Agentic Orchestration** | ~20 | Multi-model pipelines with role separation (reasoner/actor, conductor/worker). Emerging architectural pattern. |

### Tier 3: Adjacent Domains

| Category | Papers | Relationship to TTC |
|---|---|---|
| **Diffusion Inference Scaling** | ~25 | TTC techniques applied to diffusion sampling — different domain, analogous principles |
| **Retrieval & Tool Augmentation** | ~35 | Complementary to TTC — augments model with external knowledge/capabilities |
| **Uncertainty & Calibration** | ~50 | Cross-cutting concern — enables adaptive allocation, measures TTC effectiveness |

---

## Key Findings

1. **Verification is the bottleneck, not generation.** The largest technique cluster (435 grep hits for reward/verification) reflects that *evaluating* outputs is harder than *generating* candidates. Improving verifiers yields larger gains than improving search.

2. **Overthinking is the dominant efficiency problem.** ~20 papers specifically address models generating excessive, redundant reasoning. Adaptive compute allocation is an active and urgent subfield.

3. **Small models + heavy TTC can match large models.** Multiple papers demonstrate that 1.5B–7B models with extensive test-time compute match or exceed 32B–70B models with standard inference. This reshapes the cost-performance landscape.

4. **Training-free methods are rapidly growing.** Many papers propose test-time techniques requiring no fine-tuning — applicable to any base model. This is the fastest-growing design pattern.

5. **Sequential vs. parallel is the fundamental allocation tradeoff.** Papers explicitly studying whether to generate more candidates (parallel) or iterate longer (sequential) find the answer is task-dependent — parallel for diverse solution spaces, sequential for convergent refinement.

6. **Compositionality is under-studied.** Most papers propose or evaluate a single technique. The interactions between techniques (e.g., does BoN + PRM + self-refinement compose well?) remain largely unexplored.

## Open Questions

- **Optimal composition**: Which combinations of TTC techniques yield superlinear gains?
- **Generalization beyond math/code**: Most TTC scaling results are on verifiable tasks. How well do techniques transfer to open-ended generation?
- **Cost accounting**: Standardized metrics for comparing TTC methods (FLOPs per quality point, latency-adjusted accuracy) are missing.
- **Diminishing returns**: At what compute budget does TTC scaling plateau for each technique family?
- **Training-time / test-time tradeoff**: What's the optimal split between investing in better base models vs. heavier TTC?

## Paper List

See [papers.md](test_time_compute_scaling/papers.md) (987 papers).

## Extraction Artifacts

- [option_c_extraction.md](test_time_compute_scaling/option_c_extraction.md) — grep-seeded categories with paper counts
- [option_a_refinement.md](test_time_compute_scaling/option_a_refinement.md) — LLM semantic refinement pass
