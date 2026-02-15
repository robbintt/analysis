# TTA Technique Extraction — Option A (Single LLM Pass)

Extracted from 284 core_contribution summaries, ordered by prevalence.

## Recurring Technique Categories

### 1. Entropy Minimization & Variants
Minimizing prediction entropy on unlabeled test samples to adapt model parameters. Includes standard entropy minimization (TENT), ranked entropy (REM), confidence-filtered variants, and entropy-gated update scheduling.
- Representative papers: 2509.02982, 2505.05375, 2505.16441, 2509.23183, 2510.03258, 2510.11068

### 2. Batch Normalization Statistics Adaptation
Updating BN running statistics (mean/variance) using test-time batch statistics, often combined with source statistic interpolation. Some methods extend to GroupNorm/LayerNorm.
- Representative papers: 2502.12195, 2509.04977, 2505.16257, 2511.03148, 2508.16124, 2511.15276

### 3. Prompt Tuning at Test Time (TPT)
Optimizing learnable prompt tokens (text or visual) during inference for vision-language models like CLIP. Includes entropy-based optimization, augmentation-filtered consistency, and cache-based approaches.
- Representative papers: 2501.16404, 2506.22819, 2511.10481, 2511.11690, 2506.03190, 2601.08139, 2601.23253, 2601.02147

### 4. Self-Supervised Auxiliary Tasks
Using self-supervised objectives (masked reconstruction, rotation prediction, contrastive learning) as proxy losses for adaptation when no labels are available.
- Representative papers: 2509.03012, 2505.18734, 2512.15762, 2509.26301, 2507.05221, 2506.23529

### 5. Teacher-Student / EMA Frameworks
Maintaining a momentum-updated teacher model alongside an adapting student to provide stable pseudo-labels and prevent catastrophic forgetting during continual adaptation.
- Representative papers: 2511.18468, 2501.00873, 2512.18321, 2502.02998, 2510.05530

### 6. Pseudo-Labeling with Confidence Filtering
Generating pseudo-labels from model predictions, filtering by confidence or consistency, and using them as supervision for parameter updates.
- Representative papers: 2506.12481, 2511.18066, 2503.14564, 2510.03574

### 7. Feature Alignment / Distribution Matching
Aligning test-time feature distributions to source domain statistics via moment matching, optimal transport, or feature normalization.
- Representative papers: 2511.22862, 2508.04552, 2510.22127, 2512.06652, 2511.14416

### 8. Test-Time Training (TTT) with Gradient Updates
Performing actual gradient-based parameter updates at inference on each test sample or batch, typically via self-supervised loss.
- Representative papers: 2503.11842, 2509.24510, 2505.23884, 2512.23675, 2601.01605, 2512.13898, 2507.18809

### 9. Cache / Memory-Based Adaptation
Building non-parametric caches or memory banks of test-time features/predictions to support nearest-neighbor classification or prototype refinement without parameter updates.
- Representative papers: 2503.23388, 2512.11458, 2507.21494, 2511.18811, 2601.11669

### 10. Domain-Diversity / Shift Detection
Detecting the type or severity of distribution shift to trigger, modulate, or skip adaptation. Includes domain-diversity scoring and drift detection mechanisms.
- Representative papers: 2408.08056, 2601.15544, 2601.21012, 2510.03839, 2508.21278

### 11. Activation Sparsity / Memory-Efficient TTA
Reducing memory and compute costs of TTA for edge/IoT deployment via activation pruning, gradient-free optimization, or parameter-efficient updates.
- Representative papers: 2503.20354, 2510.11068, 2511.15276, 2503.15889, 2506.07078

### 12. Model Merging / Multi-Expert Routing
Combining multiple source models or experts at test time, routing inputs to appropriate experts based on test-time signals.
- Representative papers: 2502.20395, 2511.13760, 2512.22467, 2512.02441, 2510.14853

### 13. Data Augmentation at Test Time (TTA-Aug)
Generating augmented views of test inputs and aggregating predictions for robustness, without updating parameters.
- Representative papers: 2510.03574, 2507.03458, 2512.11847, 2511.10481

### 14. Diffusion Model Priors for Adaptation
Using pretrained diffusion models as priors to guide adaptation, either for score-based guidance or to refine predictions.
- Representative papers: 2501.00873, 2511.22688, 2512.17908, 2508.01975

### 15. Causal / Invariant Feature Selection
Identifying and preserving causal or invariant features while removing spurious correlations during adaptation.
- Representative papers: 2510.11133, 2507.17001, 2508.00304

### 16. Bayesian / Probabilistic Adaptation
Framing TTA as Bayesian inference — posterior updates, variational methods, or probabilistic filtering over model parameters.
- Representative papers: 2402.08182, 2503.06633, 2601.21012, 2510.13763

### 17. Continual TTA (CTTA)
Specifically addressing sequential/streaming domain shifts where the model must adapt continuously without accumulating errors or forgetting.
- Representative papers: 2505.16441, 2511.18468, 2601.15544, 2502.20677, 2505.13643

## Domain-Specific Application Clusters

- **Medical imaging**: 2502.08774, 2503.13012, 2512.06652, 2512.15762, 2601.13919
- **Autonomous driving**: 2508.12690, 2505.16524, 2512.01300
- **Speech/Audio**: 2506.11121, 2509.25495, 2601.16240, 2507.15523
- **EEG/Biosignals**: 2501.03764, 2502.06828, 2511.22030, 2509.26301
- **Federated learning**: 2503.06633, 2505.13643, 2507.21494, 2511.18066, 2508.02993
- **Graph neural networks**: 2510.07762, 2510.22289, 2511.07023
- **ARC benchmark**: 2511.02886, 2512.11847, 2511.14761, 2601.10904
