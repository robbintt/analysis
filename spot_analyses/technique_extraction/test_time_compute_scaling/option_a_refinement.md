# Test-Time Compute Scaling — LLM Refinement Pass (Option A)

**Basis:** Option C grep-seeded extraction (20 categories, 76.4% coverage, 987 papers)  
**Method:** Category-by-category semantic review of core_contribution samples, cross-category pattern analysis

---

## Structural Observations

### Category Hierarchy

The 20 grep categories reveal a natural **three-tier hierarchy** that the flat list obscures:

1. **Compute Allocation Layer** — *how much* compute to spend and *where*
   - Adaptive/Dynamic Compute, Scaling Laws/Tradeoffs, Thinking Modes
2. **Search & Generation Layer** — *how* to generate candidates
   - CoT, Tree/Graph Search, Parallel Sampling, Iterative Reasoning, Self-Refinement
3. **Evaluation & Selection Layer** — *how* to judge and select outputs
   - Reward Models (PRM/ORM), Verifiers, Uncertainty/Calibration, Voting/Consensus

Most papers combine techniques from 2+ layers (e.g., tree search + PRM + adaptive budget). The grep categories correctly capture individual techniques but miss these compositional patterns.

### Recommended Merges

1. **Merge "Search Strategies" into "Tree/Graph Search"** — The 41 "search strategy" papers substantially overlap with tree search and parallel sampling. The non-overlapping papers describe generic search concepts that belong as a cross-cutting concern, not a category.

2. **Merge "Iterative/Multi-Step Reasoning" into "Self-Refinement"** — Semantic overlap is ~70%. The distinction (iterative = multiple passes; self-refine = improving own output) is artificial. Merged category: **Iterative Self-Refinement** (~60 papers after dedup).

3. **Merge "Scaling Laws/Tradeoffs" into "Adaptive Compute"** — The scaling law papers are largely about *characterizing* the same compute allocation problem. Merged: **Compute-Optimal Allocation** (~55 papers after dedup).

4. **Keep "Thinking Modes" separate from "Adaptive Compute"** — Despite surface similarity, thinking modes papers describe *architectural mechanisms* (dual-mode models, thinking budgets, System 1/2), while adaptive compute papers describe *runtime allocation strategies*. Different interventions.

### Recommended Splits

1. **Split "Verification & Reward" (435 papers) into 4 sub-categories:**
   - **Process Reward Models (PRM)** (32 papers): Step-level reward signals for intermediate reasoning evaluation
   - **Outcome Reward Models (ORM)** (3 papers): Final-answer-only reward scoring
   - **Learned Verifiers** (~65 papers): Trained models that verify correctness/quality of outputs — includes both parametric verifiers and LLM-as-judge approaches
   - **Self-Verification** (~15 papers): Models checking their own outputs without external verifiers
   - **Formal/Symbolic Verification** (~10 papers): Using formal methods, code execution, or symbolic checks
   - **Reward Model Training** (~45 papers): Papers focused on training reward models (RLHF, generative reward models) rather than using them at inference
   - **Verification as Component** (remaining ~265 papers): Papers that *use* verification as part of a larger system but whose core contribution is elsewhere — these should be tagged but not categorized here

   The 435 number is inflated because "verification" and "reward model" are both techniques *and* components. The subcategories above separate "papers about verification" from "papers that use verification."

2. **Split "Diffusion & Continuous Reasoning" (70 papers) into:**
   - **Diffusion Model Inference Scaling** (~25 papers): Scaling compute for diffusion model sampling — more denoising steps, better samplers, inference-time search over noise
   - **Diffusion Language Models** (~15 papers): Discrete/continuous diffusion for text generation — a fundamentally different architecture for test-time compute
   - **Latent/Continuous Reasoning** (~5 papers): Continuous thought representations, latent reasoning tokens
   - **Diffusion Applications** (~25 papers): Papers applying diffusion to specific domains, tangential to test-time compute scaling

---

## Sub-Category Discovery Within Major Categories

### Chain-of-Thought / Reasoning Chains (151 papers)

Sub-categories identified from semantic review:

- **CoT Prompting & Variants** (~30 papers): Zero-shot CoT, few-shot CoT, difficulty-aware CoT, compressed CoT — the prompting-level techniques
- **CoT Training** (~35 papers): Training models to produce better reasoning traces — SFT on traces, critical token fine-tuning, reasoning distillation
- **CoT Analysis & Evaluation** (~25 papers): Papers studying CoT quality, faithfulness, failure modes, benchmarks
- **Reasoning Token Mechanisms** (~15 papers): Thinking tokens, continue-thinking tokens, pause tokens — architectural modifications for reasoning
- **Domain-Specific CoT** (~20 papers): CoT applied to vision, audio, time series, tables — transferring the paradigm beyond text
- **CoT Efficiency** (~15 papers): Reducing CoT length, compressing traces, identifying critical tokens
- **CoT + Other Techniques** (~11 papers): CoT combined with search, verification, or self-refinement

### RL-Based Training for Reasoning (102 papers)

Sub-categories:

- **GRPO/PPO for Reasoning** (~30 papers): Standard RL algorithms applied to improve reasoning — the "train to think" approach
- **RLHF/DPO Alignment** (~20 papers): Alignment-focused RL, often with reasoning as a secondary benefit
- **Reward Model Co-Training** (~15 papers): Joint training of policy and reward models (e.g., SPARK's co-evolving framework)
- **RL for Agents** (~15 papers): RL training for multi-step agent behavior, tool use, code generation
- **RL + Verification** (~12 papers): RL with verifiable rewards, rule-based RL, execution-based feedback
- **Critique/Reflection RL** (~10 papers): Training models to critique and refine via RL (CRL, reflection-based RL)

### Tree/Graph Search (43 papers)

Sub-categories:

- **MCTS-Based** (~15 papers): Monte Carlo Tree Search applied to reasoning — MCTS for proof search, planning, trajectory construction
- **Beam Search Variants** (~10 papers): Entropy-gated branching, selective beam search, confidence-based branching
- **Tree-of-Thought** (~8 papers): Explicit ToT frameworks, ToTRL (training for tree reasoning)
- **Dynamic Branching** (~5 papers): Adaptive branching strategies — branch at uncertainty, prune low-value paths
- **Graph/DAG Reasoning** (~5 papers): Graph-of-thought, non-tree structured reasoning

### Adaptive Compute + Scaling Tradeoffs (merged, ~55 papers)

Sub-categories:

- **Overthinking Mitigation** (~20 papers): Detecting and reducing excessive reasoning — early stopping, length control, batch prompting
- **Query-Adaptive Allocation** (~12 papers): Difficulty-aware compute routing, bandit-based allocation, utility optimization
- **Scaling Law Characterization** (~10 papers): Empirical scaling laws for test-time compute, compute-performance curves
- **Fast/Slow Routing** (~8 papers): Model cascading, routing between fast and slow inference paths
- **Training-Aware Scaling** (~5 papers): Joint optimization of training and test-time compute (TTC-aware training)

---

## Techniques Grep Missed

### A. Speculative Reasoning / Draft-Verify Pipelines (~12 papers)

Papers using smaller "draft" models to generate candidate reasoning steps, verified by larger models. Caught partially by "efficiency" (speculative decoding) but the *reasoning-specific* application is distinct. Example: SPECS uses draft models for reasoning step generation.

### B. Agentic Orchestration (~20 papers)

Papers where the core contribution is orchestrating multiple LLM calls, tools, and verification loops into an agent pipeline. Partially caught by "multi-agent" and "tool use" but the orchestration pattern itself is a technique: conductor models, agentic frameworks (ARTIST, AlphaApollo, Agentar-Scale-SQL).

### C. Latent/Implicit Reasoning (~8 papers)

Models that reason without explicit token generation — latent thought vectors, internal representations, continuous reasoning. Partially caught by "diffusion/continuous" but conceptually distinct. Example: LTA-Thinker generates latent thought vectors.

### D. Curriculum / Progressive Reasoning (~5 papers)

Training or inference strategies that progressively increase reasoning complexity. Caught by "curriculum" in the original grep but too few hits to surface as a category.

### E. Dual-Model Architectures (~10 papers)

Explicit separation into a reasoner and an actor/executor — not multi-agent debate, but structured role separation. Example: PRORE's reasoner-actor collaboration.

---

## Cross-Cutting Themes (Not Categories)

These appear across multiple categories and are better understood as **design principles** than technique categories:

1. **Training-Free vs. Training-Required**: Every technique family splits into methods requiring fine-tuning and training-free methods deployable on any model. The training-free methods are growing rapidly.

2. **Sequential vs. Parallel Scaling**: The fundamental allocation axis — generate more candidates in parallel (BoN, voting) or iterate sequentially (refinement, multi-turn). Several papers explicitly study this tradeoff.

3. **Verifiable vs. Open-Ended Tasks**: Test-time compute scaling shows dramatically different effectiveness on tasks with verifiable answers (math, code) vs. open-ended generation. This is a domain property, not a technique, but shapes which techniques apply.

4. **Model Size Interaction**: Multiple papers find that test-time compute scaling benefits smaller models more than larger ones, and that small models + heavy TTC can match large models with light TTC. This shapes the practical value proposition.

---

## Disagreements with Option C

1. **Diffusion category is polluted**: ~35% of the 70 "diffusion" papers are about applying test-time scaling techniques *to* diffusion models (a domain), not about diffusion *as* a reasoning technique. Should be split as recommended above.

2. **Retrieval/Tool Use is tangential**: The 38 RAG/tool-use papers are largely about augmenting models with external knowledge or capabilities — adjacent to but distinct from "scaling inference compute." These are better understood as *complements* to test-time compute scaling rather than instances of it.

3. **RL Training category conflates training and inference**: The 102 RL papers include both "train with RL to reason better" (training-time technique) and "use RL-style search at inference" (test-time technique). These are fundamentally different — one changes the model, the other changes the inference procedure.

4. **Reward/Verification count (435) overstates the category**: As noted in the split recommendation, most of these papers *use* verification rather than *contributing* verification techniques. The true "verification technique" papers number ~120.

---

## Final Recommended Taxonomy

### Tier 1: Core Test-Time Scaling Techniques

| Category | Est. Papers | Description |
|---|---|---|
| Chain-of-Thought & Reasoning Traces | ~100 | Explicit verbalized reasoning (prompting, training, architectural) |
| Tree/Graph Search | ~45 | Structured search over reasoning paths (MCTS, beam, ToT) |
| Best-of-N & Parallel Sampling | ~50 | Generate multiple candidates, select via voting/scoring |
| Iterative Self-Refinement | ~55 | Sequential improvement of outputs through reflection/correction |
| Process Reward Models | ~32 | Step-level reward signals for intermediate evaluation |
| Learned Verifiers | ~65 | Trained models for output verification and selection |
| Adaptive Compute Allocation | ~50 | Dynamic compute budgeting based on difficulty/confidence |

### Tier 2: Enabling Techniques

| Category | Est. Papers | Description |
|---|---|---|
| RL Training for Reasoning | ~80 | Training models via RL to reason better (enables Tier 1) |
| Thinking Modes & Architecture | ~20 | Dual-mode models, thinking budgets, System 1/2 |
| Reasoning Distillation | ~45 | Compressing TTC capabilities into efficient models |
| Efficiency & Acceleration | ~40 | Speculative decoding, caching, pruning for faster TTC |
| Agentic Orchestration | ~20 | Multi-model pipelines, conductor models, role separation |

### Tier 3: Adjacent / Application Domains

| Category | Est. Papers | Description |
|---|---|---|
| Diffusion Model Inference Scaling | ~25 | TTC techniques applied to diffusion sampling |
| Retrieval & Tool Augmentation | ~35 | RAG, tool use as inference-time augmentation |
| Uncertainty & Calibration | ~50 | Confidence estimation, calibration (cross-cuts Tier 1) |
| Domain-Specific Applications | ~40 | Vision, audio, code, medical, etc. |

### Unmatched (~233 papers)

Benchmarks, evaluations, surveys, tangential mentions. Expected and acceptable.
