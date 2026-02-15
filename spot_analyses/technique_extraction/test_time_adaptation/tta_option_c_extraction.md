# TTA Technique Extraction — Option C (Grep-Seeded Categories)

Extracted via term-frequency seeding across 284 core_contribution summaries.
Coverage: 200/284 papers matched (70%). Remaining 84 are tangential, domain-specific applications, benchmarks without novel TTA techniques, or empty entries.

## Technique Categories (by paper count)

### 1. Teacher-Student / EMA Frameworks (33 papers)
Momentum-updated teacher provides stable targets for adapting student. Includes dual-teacher (slow/fast), mean teacher, EMA weight anchoring.

### 2. Test-Time Training — TTT (30 papers)
Gradient-based parameter updates at inference via self-supervised or task-specific losses. Includes TTT layers, next-token prediction TTT, and RL-based TTT.

### 3. Edge / Memory-Efficient TTA (25 papers)
Gradient-free, activation-sparse, quantized, or parameter-efficient methods targeting deployment on edge/mobile/IoT devices.

### 4. Benchmark / Survey (24 papers)
Evaluation frameworks, comprehensive surveys, and systematic comparisons of TTA methods across domains.

### 5. RL / Policy Adaptation at Test Time (19 papers)
Adapting RL policies, embodied agents, or agentic systems to new environments at deployment without retraining.

### 6. Open-Set / OOD Detection (19 papers)
Handling unknown classes or out-of-distribution samples during adaptation, including open-set TTA and OOD-aware adaptation.

### 7. Test-Time Augmentation (19 papers)
Generating augmented views of test inputs and aggregating predictions. Includes multi-crop, Fourier-space, and domain-simulating augmentations.

### 8. Domain Generalization / Source-Free (17 papers)
Adapting without access to source data. Includes source-free domain adaptation and methods that generalize to unseen domains.

### 9. Entropy Minimization (16 papers)
Minimizing prediction entropy on unlabeled test samples. Includes TENT, ranked entropy, entropy gating, and entropy-aware scheduling.

### 10. Continual TTA — CTTA (16 papers)
Sequential/streaming domain shifts requiring continuous adaptation without error accumulation or catastrophic forgetting.

### 11. Batch Normalization Adaptation (15 papers)
Updating BN statistics at test time, interpolating with source statistics, extending to GroupNorm/LayerNorm.

### 12. Self-Supervised Auxiliary Tasks (15 papers)
Proxy losses (masked reconstruction, rotation, contrastive) for adaptation when no labels are available.

### 13. Distribution / Feature Alignment (11 papers)
Aligning test features to source statistics via moment matching, optimal transport, or statistical alignment.

### 14. Bayesian / Probabilistic Adaptation (11 papers)
Posterior updates, variational methods, Bayesian filtering over parameters or predictions.

### 15. Prompt Tuning at Test Time (10 papers)
Optimizing learnable prompts during inference for VLMs like CLIP. Includes entropy-based, cache-augmented, and attribute-aware variants.

### 16. Model Merging / Multi-Expert Routing (10 papers)
Combining models or routing to specialized experts at test time based on input characteristics.

### 17. Pseudo-Labeling with Filtering (8 papers)
Generating and filtering pseudo-labels by confidence or consistency for self-training during adaptation.

### 18. Federated TTA (7 papers)
Test-time adaptation in federated learning settings with privacy constraints and decentralized data.

### 19. Cache / Memory-Based Adaptation (6 papers)
Non-parametric caches, memory banks, or nearest-neighbor retrieval supporting adaptation without parameter updates.

### 20. Meta-Learning for TTA (6 papers)
MAML-style or bi-level optimization to learn how to adapt at test time.

### 21. Shift / Drift Detection (4 papers)
Detecting distribution shift type or severity to trigger, modulate, or skip adaptation.

## Coverage Gaps (84 unmatched)

Many unmatched papers are:
- Domain-specific applications that mention TTA tangentially
- Benchmarks/datasets without proposing new TTA techniques
- Papers where TTA is a minor component of a larger system
- 2 empty entries (no core_contribution text)
