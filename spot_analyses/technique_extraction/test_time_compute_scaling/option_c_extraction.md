# Test-Time Compute Scaling — Grep-Seeded Technique Extraction (Option C)

**Corpus:** 987 papers from `spot_analysis_paper_groups` (group: `test_time_compute_scaling`)  
**Coverage:** 754/987 (76.4%) papers matched to at least one category  
**Unmatched:** 233 papers — predominantly benchmarks, evaluations, and domain-specific applications that mention test-time/inference-time in passing rather than proposing techniques.

---

## Categories

### 1. Verification & Reward-Based Guidance (435 papers)

Largest category. Papers using verification signals or reward models to guide inference-time computation. Contains clear sub-groups:

- **Verifier-based** (97 papers): Explicit verifiers that check or score candidate outputs. Includes formal verification, self-verification, and learned verifiers.
- **Reward Model** (66 papers): General reward models guiding generation — both for training and inference-time scoring/ranking.
- **Process Reward Models / PRM** (32 papers): Step-level reward signals that evaluate intermediate reasoning steps rather than final answers.
- **Outcome Reward Models / ORM** (3 papers): Reward models that score only final outputs.
- **Self-evaluation** (small overlap with self-refine): Models evaluating their own outputs.

Pattern: `process.reward|outcome.reward|reward.model|verif\w*|self.verif|self.evaluat|prm|orm`

### 2. Chain-of-Thought / Reasoning Chains (151 papers)

Explicit verbalized reasoning — chain-of-thought prompting and variants, reasoning trace analysis, thinking tokens, step-level and token-level reasoning granularity.

Pattern: `chain.of.thought|\bcot\b|reasoning.chain|reasoning.trace|reasoning.step|thinking.token|step.level|token.level`

### 3. RL-Based Training for Reasoning (102 papers)

Reinforcement learning methods to train or fine-tune models for better reasoning. GRPO, PPO, DPO, RLHF, policy gradient methods, self-play, actor-critic architectures.

Pattern: `reinforcement.learn\w*|rl.based|\bgrpo\b|\bppo\b|\bdpo\b|\brlhf\b|policy.gradient|self.play|advantage|actor.critic`

### 4. Diffusion & Continuous Reasoning (70 papers)

Diffusion models, flow matching, consistency models applied to reasoning or generation. Includes latent/continuous thought representations.

Pattern: `diffusion|flow.matching|consistency.model|latent.reason|continuous.thought`

### 5. Uncertainty & Calibration (58 papers)

Uncertainty quantification, calibration, entropy-based methods, abstention, refusal, confidence estimation at inference time.

Pattern: `uncertainty|calibrat\w*|entropy|abstain|refusal|confiden\w*`

### 6. Best-of-N / Parallel Sampling / Voting (54 papers)

Generate multiple candidates in parallel, then select the best via voting, consensus, self-consistency, or ensemble methods.

Pattern: `best.of.n|majority.voting|self.consistency|parallel.sampling|consensus|voting|ensemble`

### 7. Distillation (48 papers)

Knowledge distillation of reasoning capabilities — compressing expensive inference-time computation into smaller/faster models. Teacher-student setups.

Pattern: `distill\w*|knowledge.distill|teacher.student|compress`

### 8. Self-Refinement / Correction (47 papers)

Iterative self-improvement at inference time — self-refine, self-correct, sequential revision, reflection, introspection.

Pattern: `self.refine|self.correct|sequential.revision|self.improv|iterative.refine|reflect\w*|introspect`

### 9. Tree/Graph Search (43 papers)

Structured search over reasoning paths — tree-of-thought, MCTS, beam search, graph-of-thought, backtracking, lookahead.

Pattern: `tree.of.thought|\btot\b|\bgot\b|monte.carlo|\bmcts\b|beam.search|lookahead|backtrack|tree.search|graph.of.thought|thought.propag`

### 10. Inference Efficiency (43 papers)

Speculative decoding, KV cache optimization, pruning, sparsity — making inference-time computation cheaper or faster.

Pattern: `speculative|kv.cache|pruning|sparse|efficient.infer`

### 11. Search Strategies (41 papers)

Explicit search algorithms and exploration-exploitation tradeoffs at inference time. Sampling strategies.

Pattern: `search.strateg|search.algorithm|exploration|exploit|test.time.search|inference.time.search|sampling.strateg`

### 12. Retrieval-Augmented / Tool Use (38 papers)

RAG, retrieval-augmented generation, tool use, code execution as inference-time compute augmentation.

Pattern: `retrieval.augment|\brag\b|tool.use|code.execut`

### 13. Adaptive / Dynamic Compute Allocation (34 papers)

Dynamic allocation of compute budget — early exit, layer skipping, confidence-based routing, overthinking/underthinking analysis, compute-optimal strategies, scaling laws.

Pattern: `adaptive.compute|dynamic.compute|compute.allocat|budget.allocat|early.exit|layer.skip|exit.layer|confidence.based|compute.optimal|overthink|underthink|scaling.law`

### 14. Scaling Laws & Compute Tradeoffs (34 papers)

Scaling laws for test-time compute, FLOP analysis, cost-performance tradeoffs, Pareto frontiers.

Pattern: `scaling.law|compute.performance|flop|inference.cost|compute.efficien|cost.performance|pareto|tradeoff|trade.off`

### 15. Iterative / Multi-Step Reasoning (30 papers)

Multi-turn, multi-round, multi-step, sequential reasoning approaches. Iterative inference procedures.

Pattern: `iterative.reason|multi.turn|multi.round|multi.step|sequential.reason|iterative.infer`

### 16. Planning & World Models (28 papers)

Planning algorithms, world models, internal models, meta-cognition, meta-learning for inference-time reasoning.

Pattern: `planning|world.model|internal.model|meta.cognit|meta.learn`

### 17. Multi-Agent / Debate (22 papers)

Multi-agent collaboration, debate between models, agent discussion for inference-time computation.

Pattern: `multi.agent|debate|agent.collabor|agent.discuss`

### 18. Inference-Time Intervention & Steering (17 papers)

Direct activation/representation engineering at inference — mode steering, activation steering, inference-time alignment, test-time training, representation engineering.

Pattern: `inference.time.interven|inference.time.optim|test.time.optim|mode.steer|activation.steer|inference.time.align|test.time.train|representation.engineer`

### 19. Thinking Modes (16 papers)

Explicit slow/fast thinking modes, thinking budgets, System 1/2 analogies, wait/pause tokens, deep thinking toggles.

Pattern: `slow.think|fast.think|system.1|system.2|thinking.mode|thinking.budget|non.thinking|wait.token|pause.token|long.think|short.think|deep.think`

### 20. Prompt Optimization (15 papers)

Prompt engineering, prompt refinement, prompt adaptation, in-context learning, few-shot prompting as inference-time techniques.

Pattern: `prompt.optim|prompt.engineer|prompt.refin|prompt.adapt|in.context.learn|few.shot.prompt`

---

## Coverage Gaps

233 unmatched papers (23.6%) fall into:

- **Benchmarks/Evaluations** (~40%): Papers creating or using benchmarks that happen to evaluate test-time scaling behavior but don't propose new techniques.
- **Domain applications** (~25%): Papers applying test-time methods to specific domains (medical, legal, robotics) where the core contribution is the application rather than the technique.
- **Tangential mentions** (~20%): Papers that mention "test-time" or "inference-time" incidentally (e.g., "test-time augmentation" in vision, latency measurements).
- **Niche techniques** (~15%): Papers with unique approaches not captured by the 20 categories above.

## Notes

- Many papers span multiple categories (e.g., RL training + PRM + tree search). The categories are not mutually exclusive.
- The reward/verification supercategory (435 papers) is disproportionately large because verification is both a standalone technique and a component used within many other techniques (search, sampling, self-refinement).
- Diffusion (70 papers) includes many papers where diffusion models are the *application domain* for test-time compute scaling rather than a *technique* for scaling compute.
